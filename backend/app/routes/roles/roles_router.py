from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.roles.role_model import Role
from app.models.tenants.tenant_model import Tenant
from app.schemas.roles.roles_schema import (
    AssignRoleToUser,
    CreateRoleSchema,
    RoleReponseSchema,
    UpdateRoleSchema,
)

roles_router = APIRouter()


# we will get all the routes
@roles_router.get(
    "/", status_code=status.HTTP_200_OK, response_model=list[RoleReponseSchema]
)
async def get_roles(session: Annotated[AsyncSession, Depends(app_session)]):
    """This will fetch all the available roles"""
    statement = await session.execute(select(Role))
    results = statement.scalars().all()
    return results


@roles_router.post("")
async def create_role(
    role_data: CreateRoleSchema, session: Annotated[AsyncSession, Depends(app_session)]
):
    """This will be used to create new roles"""
    role_data_dict = role_data.model_dump()

    statement = await session.execute(
        select(func.lower(Role.name) == role_data_dict["name"].lower())
    )
    available_roles = statement.scalars().all()
    for role in available_roles:
        if role:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Role with that name already exsists",
            )
        # we will add the role here
    new_role = Role(**role_data_dict)
    session.add(new_role)
    await session.commit()
    return new_role


@roles_router.patch("/{role_id}")
async def update_role(
    role_id: int,
    role_data: UpdateRoleSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will update the role"""
    statement = await session.execute(select(Role).where(Role.id == role_id))
    role = statement.scalars().first()

    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role with that id does not exists",
        )

    role_to_update = role_data.model_dump(exclude_unset=True)
    for key, value in role_to_update.items():
        setattr(role, key, value)

    await session.commit()
    return role


@roles_router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_role(
    role_id: int, session: Annotated[AsyncSession, Depends(app_session)]
):
    """We will delete the role in the database based on the passed id"""
    statement = await session.execute(select(Role).where(Role.id == role_id))
    role = statement.scalars().first()

    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role with that id does not exists",
        )

    await session.delete(role)
    await session.commit()


@roles_router.post("/assign-roles")
async def assign_role_to_user(
    roled_data: AssignRoleToUser, session: Annotated[AsyncSession, Depends(app_session)]
):

    statement = await session.execute(select(Role).where(Role.id == roled_data.role_id))
    role = statement.scalars().first()

    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role with that id does not exists",
        )

    # we will grab the passed user id
    statement = await session.execute(
        select(Tenant).where(Tenant.id == roled_data.tenant_id)
    )
    tenant = statement.scalars().first()
    if not tenant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tenant with that id does not exists",
        )

    # we will assign the roles here
    new_tenant = Tenant.roles[role]
    session.add(new_tenant)
    await session.commit()
    return new_tenant
