from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class AppSettings(BaseSettings):
    host: str
    port: int
    username: str
    database: str
    password: str
    drivername: str

    secret_key: SecretStr
    algorithm: str
    access_token_expiry_days: int = 2
    Issuer: str
    max_image_size_bytes: int = 5 * 1024 * 1024

    # for the database url
    @property
    def database_url(self):
        return URL.create(
            drivername=self.drivername,
            host=self.host,
            port=self.port,
            password=self.password,
            username=self.username,
            database=self.database,
        )

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


AppSettings = AppSettings()  # type: ignore
