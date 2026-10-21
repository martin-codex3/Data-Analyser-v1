from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.roles.role_model import Role
from app.models.tenants.tenant_model import Tenant
from app.schemas.tenants.tenant_schemas import CreateTenantSchema

tenant_routes = APIRouter()


@tenant_routes.post("/sign-in")
async def create_tenant_account(
    tenant_data: CreateTenantSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will create the tenant account"""
    tenant_data_dict = tenant_data.model_dump()

    statement = await session.execute(
        select(Tenant).where(func.lower(Tenant.email == tenant_data.email))
    )
    tenant = statement.scalars().first()

    if not tenant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email or Password is incorrect",
        )

    # we will fetch all the available roles here
    statement = await session.execute(
        select(Role).where(func.lowe(Role.name == "admin"))
    )
    role = statement.scalars().first()

    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cannot assign that role"
        )

    new_tenant = Tenant(**tenant_data_dict)
    session.add(new_tenant)
    await session.commit()

    # we will assign the role to the user here
    new_tenant.roles = [role]

    return new_tenant
