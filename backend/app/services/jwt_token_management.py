from datetime import UTC, datetime, timedelta

import jwt

from app.config.settings.app_settings import AppSettings


class Token:
    acess_token: str
    token_type: str


async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expires = datetime.now(UTC) + expires_delta
    else:
        expires = datetime.now(UTC) + timedelta(
            minutes=AppSettings.access_token_expiry_minutes
        )

    to_encode.update({"exp": expires})
    jwt_encoded = jwt.encode(to_encode, AppSettings.secret_key, AppSettings.algorithm)
    return jwt_encoded
