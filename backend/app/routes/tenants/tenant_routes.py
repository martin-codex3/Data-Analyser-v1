import uuid
from datetime import UTC, datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.config.settings.app_settings import AppSettings
from app.models.roles.role_model import Role
from app.models.tenants.tenant_model import Tenant
from app.schemas.tenants.tenant_schemas import CreateTenantSchema, TenantResponseSchema
from app.services.jwt_token_management import Token, create_access_token
from app.services.password_management import hash_tenant_password
from app.services.tenant_service import get_current_tenant

tenant_routes = APIRouter()


@tenant_routes.post(
    "/create-account",
    status_code=status.HTTP_201_CREATED,
    response_model=TenantResponseSchema,
)
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

    if tenant:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # we will fetch all the available roles here
    statement = await session.execute(
        select(Role).where(func.lower(Role.name == "admin"))
    )
    role = statement.scalars().first()

    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cannot assign that role"
        )

    new_tenant = Tenant(**tenant_data_dict)
    new_tenant.password_hash = hash_tenant_password(new_tenant.password_hash)
    # we will assign the role to the user here
    new_tenant.roles = [role]
    session.add(new_tenant)
    await session.commit()

    return new_tenant


# for authenticating the tenants
@tenant_routes.post("/token")
async def login_for_access_token(
    tenant_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """We will authenticate the tenant using their username and password"""
    statement = await session.execute(
        select(Tenant).where(func.lower(Tenant.email) == tenant_data.username)
    )

    tenant = statement.scalars().first()
    if not tenant:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expiry = timedelta(minutes=AppSettings.access_token_expiry_minutes)
    # we will generate the access token here
    access_token = create_access_token(
        data={
            "sub": str(tenant.id),
            "jti": str(uuid.uuid4()),
            "iat": datetime.now(UTC),
            "exp": AppSettings.access_token_expiry_minutes,
            "iss": AppSettings.Issuer,
        },
        expires_delta=access_token_expiry,
    )
    return Token(access_token=access_token, token_type="bearer")


@tenant_routes.get("/me", status_code=status.HTTP_200_OK)
async def read_tenant(current_tenant: Annotated[Tenant, Depends(get_current_tenant)]):
    return current_tenant
