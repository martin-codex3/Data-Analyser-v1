import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.application_users.application_user import ApplicationUser
from app.schemas.application_users.application_user_schemas import (
    UpdateApplicationUserSchema,
)
from app.services.tenant_service import CurrentUser, get_current_tenant

users_routes = APIRouter()


@users_routes.patch("/{user_id}")
async def update_user_account(
    user_id: uuid.UUID,
    current_user: Annotated[ApplicationUser, Depends(get_current_tenant)],
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
    return "Updated"


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
