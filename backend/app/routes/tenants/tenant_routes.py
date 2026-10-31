import uuid
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.config.settings.app_settings import AppSettings
from app.models.application_users.application_user import ApplicationUser
from app.models.roles.role_model import Role
from app.models.tenant_users.tenant_user import TenantUsers
from app.models.tenants.tenant_model import Tenant
from app.schemas.tenant_users.tenant_user_schema import CreateTenantUserSchema
from app.services.jwt_token_management import Token, create_access_token
from app.services.password_management import hash_tenant_password

tenant_routes = APIRouter()


@tenant_routes.post(
    "/create-tenant-account",
    response_model=Token,
    status_code=status.HTTP_200_OK,
)
async def create_tenant_account(
    tenant_user_data: CreateTenantUserSchema,
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

        # we will check if the user already exists here
        statement = await session.execute(
            select(ApplicationUser).where(
                func.lower(ApplicationUser.email) == tenant_user_data.email,
            )
        )

        user = statement.scalars().first()

        if user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Email already registered",
            )

        # we will now create the user
        new_user = ApplicationUser(
            first_name=tenant_user_data.first_name,
            last_name=tenant_user_data.last_name,
            phone_number=tenant_user_data.phone_number,
            email=tenant_user_data.email,
            password_hash=hash_tenant_password(
                tenant_user_data.password_hash,
            ),
        )

        session.add(new_user)
        await session.flush()

        # we will check the business name
        statement = await session.execute(
            select(Tenant).where(
                func.lower(Tenant.business_name)
                == tenant_user_data.business_name.lower()
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
            business_type=tenant_user_data.business_type,
            business_name=tenant_user_data.business_name,
            business_email=tenant_user_data.business_email,
            business_phone=tenant_user_data.business_phone,
            address_line_1=tenant_user_data.address_line_1,
        )

        session.add(new_tenant)
        await session.flush()

        # we will assign the role here
        new_tenant_user = TenantUsers(
            tenant_id=new_tenant.id, application_user_id=new_user.id, role=role.name
        )

        await session.flush()

        session.add(new_tenant_user)

        await session.commit()

        # after commiting we will create the access token here
        expire_delta = timedelta(minutes=AppSettings.access_token_expiry_minutes)
        token_data = {
            "user_id": str(new_user.id),
            "sub": str(new_tenant.id),
            "email": new_user.email,
            "issuer": "StrideTechnologies",
            "jti": str(uuid.uuid4()),
            "exp": AppSettings.access_token_expiry_minutes,
            "audience": "StrideTechnologies",
        }

        access_token = create_access_token(data=token_data, expires_delta=expire_delta)
        return Token(access_token=access_token, token_type="bearer")
