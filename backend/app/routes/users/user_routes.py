import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.application_users.application_user import ApplicationUser
from app.schemas.application_users.application_user_schemas import (
    UpdateApplicationUserSchema,
)
from app.services.tenant_service import CurrentUser

users_routes = APIRouter()


@users_routes.patch("/{user_id}")
async def update_user_account(
    user_id: uuid.UUID,
    current_user: CurrentUser,
    application_user_data: UpdateApplicationUserSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """We will update the user data here"""
    application_user_data_dict = application_user_data.model_dump(exclude_unset=True)

    statement = await session.execute(
        select(ApplicationUser).where(
            func.lower(ApplicationUser.email) == current_user.email.lower()
        )
    )

    application_user = statement.scalars().first()

    if application_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorised",
            headers={"WWW-AUthenticate": "Bearer"},
        )

    # we will check if the IDs match
    if user_id is not current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorised",
            headers={"WWW-AUthenticate": "Bearer"},
        )

    # we will update the application user here
    for keys, values in application_user_data_dict.items():
        setattr(application_user, keys, values)

    await session.commit()
    await session.refresh(application_user)
    return application_user


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
