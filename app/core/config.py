from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    anthropic_api_key: str
    app_name: str = "ContentForge"
    app_version: str = "0.1.0"

@lru_cache
def get_settings() -> Settings:
    return Settings()