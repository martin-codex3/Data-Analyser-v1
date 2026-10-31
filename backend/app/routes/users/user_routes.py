import uuid
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.config.settings.app_settings import AppSettings
from app.models.application_users.application_user import ApplicationUser
from app.models.tenant_users.tenant_user import TenantUsers
from app.schemas.application_users.application_user_schemas import (
    UpdateApplicationUserSchema,
)
from app.services.jwt_token_management import Token, create_access_token
from app.services.password_management import verify_password
from app.services.tenant_service import CurrentUser

users_routes = APIRouter()


@users_routes.post("/token")
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


@users_routes.patch("/{user_id}")
async def update_user_account(
    user_id: uuid.UUID,
    current_user: CurrentUser,
    application_user_data: UpdateApplicationUserSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """We will update the user data here"""
    application_user_data_dict = application_user_data.model_dump(exclude_unset=True)

    print("Authenticated user ID:", current_user.id)
    print("Requested user ID:", user_id)
    print("IDs match:", current_user.id == user_id)

    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to update this account",
            headers={"WWW-AUthenticate": "Bearer"},
        )

    # we will update the application user here
    for keys, values in application_user_data_dict.items():
        setattr(current_user, keys, values)

    await session.commit()
    await session.refresh(current_user)
    return current_user


@users_routes.delete("/{user_id}")
async def delete_user_account(
    user_id: uuid.UUID,
    current_user: CurrentUser,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will delete the user account"""
    if user_id is not current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorised",
            headers={"WWW-AUthenticate": "Bearer"},
        )

    await session.delete(current_user)
    await session.commit()
