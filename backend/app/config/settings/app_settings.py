from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    public_database_url: str
    secret_key: SecretStr
    algorithm: str
    access_token_expiry_minutes: int = 2
    Issuer: str
    max_image_size_bytes: int = 5 * 1024 * 1024

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


AppSettings = AppSettings()  # type: ignore
