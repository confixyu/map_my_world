import os
from pydantic_settings import BaseSettings, SettingsConfigDict


script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
env_file_path = os.path.join(project_root, ".env")


class Settings(BaseSettings):
    DEBUG: bool = True
    PORT_SERVER: int = 8000
    MS_NAME: str = "map_my_world"
    API_PREFIX: str = "api/v1"
    API_STR: str = f"/{API_PREFIX}"

    model_config = SettingsConfigDict(env_file=env_file_path)


settings = Settings()
