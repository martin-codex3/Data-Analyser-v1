import uuid
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.config.settings.app_settings import AppSettings
from app.models.application_users.application_user import ApplicationUser
from app.models.roles.role_model import Role
from app.models.tenant_users.tenant_user import TenantUsers
from app.models.tenants.tenant_model import Tenant
from app.schemas.tenants.tenant_schemas import CreateTenantSchema, TenantResponseSchema
from app.services.jwt_token_management import Token, create_access_token
from app.services.password_management import hash_tenant_password, verify_password
from app.services.tenant_service import CurrentUser

tenant_routes = APIRouter()


@tenant_routes.post(
    "/create-account",
    response_model=TenantResponseSchema,
    status_code=status.HTTP_200_OK,
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

        # we will check if the user already exists here
        statement = await session.execute(
            select(ApplicationUser).where(
                func.lower(ApplicationUser.email) == tenant_data.email,
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
            first_name=tenant_data.first_name,
            last_name=tenant_data.last_name,
            phone_number=tenant_data.phone_number,
            email=tenant_data.email,
            password_hash=hash_tenant_password(
                tenant_data.password_hash,
            ),
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
        await session.flush()

        # we will assign the role here
        new_tenant_user = TenantUsers(
            tenant_id=new_tenant.id, application_user_id=new_user.id, role=role.name
        )

        session.add(new_tenant_user)

        await session.commit()
        return {
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "phone_number": new_user.phone_number,
            "address": new_tenant.address,
            "nationality": new_tenant.nationality,
            "email": new_user.email,
            "business_name": new_tenant.business_name,
            "business_type": new_tenant.business_type,
        }


@tenant_routes.post("/token")
async def login_to_create_token(
    tenant_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[AsyncSession, Depends(app_session)],
):

    statement = await session.execute(
        select(ApplicationUser).where(
            func.lower(ApplicationUser.email) == tenant_data.username
        )
    )

    user = statement.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Email or password is incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not verify_password(tenant_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Email or password is incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    statement = await session.execute(
        select(TenantUsers).where(TenantUsers.application_user_id == user.id)
    )

    tenant_user = statement.scalars().first()

    if tenant_user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot find the specified condition",
            headers={"WWW-Authenticate": "Bearer"},
        )

    expire_delta = timedelta(minutes=AppSettings.access_token_expiry_minutes)
    token_data = {
        "user_id": str(user.id),
        "sub": str(tenant_user.tenant_id),
        "email": user.email,
        "issuer": "StrideTechnologies",
        "jti": str(uuid.uuid4()),
        "exp": AppSettings.access_token_expiry_minutes,
        "audience": "StrideTechnologies",
    }

    access_token = create_access_token(data=token_data, expires_delta=expire_delta)
    return Token(access_token=access_token, token_type="bearer")


@tenant_routes.get(
    "/me", response_model=TenantResponseSchema, status_code=status.HTTP_200_OK
)
async def current_user(
    current_user: CurrentUser,
):
    return current_user


@tenant_routes.patch("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user():
    pass
