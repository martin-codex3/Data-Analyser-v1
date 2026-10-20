from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    public_database_url: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


AppSettings = AppSettings()  # type: ignore
