from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os


class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), f"../.env.{os.environ.get('ENV', 'development')}")
    )

    
@lru_cache
def get_settings():
    return Settings()
