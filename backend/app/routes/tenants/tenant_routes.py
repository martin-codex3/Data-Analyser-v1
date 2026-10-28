from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.application_users.application_user import ApplicationUser
from app.models.roles.role_model import Role
from app.models.tenants.tenant_model import Tenant
from app.schemas.tenants.tenant_schemas import CreateTenantSchema

tenant_routes = APIRouter()


@tenant_routes.post(
    "/create-account",
)
async def create_tenant_account(
    tenant_data: CreateTenantSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    async with session.begin():
        statement = await session.execute(
            select(Role).where(
                func.lower(Role.name) == "admin",
            )
        )

        role = statement.scalars().first()

        if role is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="That role does not exists",
            )

        # we will now create the user
        new_user = ApplicationUser(
            first_name=tenant_data.first_name,
            last_name=tenant_data.last_name,
            phone_number=tenant_data.phone_number,
            email=tenant_data.email,
            password_hash=tenant_data.password_hash,
        )

        session.add(new_user)
        await session.flush()

        # we will check the business name
        statement = await session.execute(
            select(Tenant).where(
                func.lower(Tenant.business_name) == tenant_data.business_name
            )
        )

        tenant = statement.scalars().first()
        if tenant:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="That name is already used",
            )

        # we will create the tenant here
        new_tenant = Tenant(
            business_name=tenant_data.business_name,
            business_type=tenant_data.business_type,
            address=tenant_data.address,
            nationality=tenant_data.nationality,
        )

        session.add(new_tenant)
        await session.commit()
        return new_tenant
