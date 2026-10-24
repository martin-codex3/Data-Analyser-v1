from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select, func
from app.services.jwt_token_management import decode_access_token

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_tenant(token: Annotated[str, Depends(oauth_scheme)]):
    """We will get the current logged in tenant"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    tenant = decode_access_token(access_token=token)
    tenant_id = tenant.get("id")

    if tenant_id is None:
        raise credentials_exception

    # we will attempt to get the user based on the id 
    tenant = 