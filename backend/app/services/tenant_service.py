import uuid
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select

from app.config.database.app_database import Session
from app.models.application_users.application_user import ApplicationUser
from app.models.tenants.tenant_model import Tenant
from app.services.jwt_token_management import decode_access_token

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/api/tenants/token")


# for the database session here
async def get_current_tenant(token: Annotated[str, Depends(oauth_scheme)]):
    """We will get the current logged in tenant"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(access_token=token)
        tenant_id = uuid.UUID(payload.get("sub"))
        user_id = uuid.UUID(payload.get("user_id"))

        if tenant_id is None:
            raise credentials_exception

        if user_id is None:
            raise credentials_exception

    except (TypeError, ValueError, jwt.InvalidTokenError):
        raise credentials_exception

    # we will attempt to get the user based on the id
    async with Session() as session:
        statement = await session.execute(select(Tenant).where(Tenant.id == tenant_id))
        tenant = statement.scalars().first()

        if tenant is None:
            raise credentials_exception

        # we will also fetch the user here
        statement = await session.execute(
            select(ApplicationUser).where(ApplicationUser.id == user_id)
        )
        user = statement.scalars().first()

        if user is None:
            raise credentials_exception

        return tenant
