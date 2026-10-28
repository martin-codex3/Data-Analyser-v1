from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.application_users.application_user import ApplicationUser
from app.models.roles.role_model import Role
from app.models.tenants.tenant_model import Tenant
from app.schemas.tenants.tenant_schemas import CreateTenantSchema
from app.services.password_management import hash_tenant_password

tenant_routes = APIRouter()


@tenant_routes.post(
    "/create-account",
)
async def create_tenant_account(
    tenant_data: CreateTenantSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    "For creating new tenant account"
    statement = await session.execute(
        select(ApplicationUser).where(
            func.lower(ApplicationUser.email) == tenant_data.email.lower()
        )
    )

    user = statement.scalars().first()

    if user:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with that email already registered",
        )

    new_user_dict = {
        "first_name": tenant_data.first_name,
        "last_name": tenant_data.last_name,
        "phone_number": tenant_data.phone_number,
        "email": tenant_data.email,
        "password_hash": hash_tenant_password(tenant_data.password_hash),
    }

    new_user = ApplicationUser(**new_user_dict)

    session.add(new_user)
    await session.commit()

    # we will check if the role exists
    statement = await session.execute(
        select(Role).where(func.lower(Role.name) == "admin".lower())
    )

    role = statement.scalars().first()

    if not role:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="That role does not exists",
        )

    # we the create the tenant here
    statement = await session.execute(
        select(Tenant).where(
            func.lower(Tenant.business_name) == tenant_data.business_name.lower()
        )
    )

    tenant = statement.scalars().first()

    if tenant:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tenant with that name already registered",
        )

    new_tenant_dict = {
        "business_name": tenant_data.business_name,
        "business_type": tenant_data.business_type,
        "address": tenant_data.address,
        "nationality": tenant_data.nationality,
    }

    new_tenant = Tenant(**new_tenant_dict)

    session.add(new_tenant)
    await session.commit()
