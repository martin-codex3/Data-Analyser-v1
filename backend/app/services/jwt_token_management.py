from datetime import UTC, datetime, timedelta

import jwt
from pydantic import BaseModel

from app.config.settings.app_settings import AppSettings


class Token(BaseModel):
    access_token: str
    token_type: str


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expires = datetime.now(UTC) + expires_delta
    else:
        expires = datetime.now(UTC) + timedelta(
            minutes=AppSettings.access_token_expiry_minutes
        )

    to_encode.update({"exp": expires})
    jwt_encoded = jwt.encode(
        to_encode, AppSettings.secret_key.get_secret_value(), AppSettings.algorithm
    )
    return jwt_encoded
