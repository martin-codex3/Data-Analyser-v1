from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.roles.role_model import Role
from app.schemas.roles.roles_schema import CreateRoleSchema, RoleReponseSchema

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
