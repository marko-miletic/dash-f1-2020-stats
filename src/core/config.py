from typing import Optional, Any
from pydantic import BaseSettings, BaseModel, \
    PostgresDsn, validator

from os import getenv
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "dash-stats-app"

    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str]) -> Any:
        if isinstance(v, str):
            return v
        
        return PostgresDsn.build(
            scheme="postgresql",
            user=getenv("POSTGRES_USER"),
            password=getenv("POSTGRES_PASSWORD"),
            host="db",
            port=getenv("POSTGRES_PORT"),
            path=f"/{getenv('POSTGRES_DB') or ''}"
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


class AppServerSettings(BaseModel):
    DEBUG: bool = True
    HOST: str = '0.0.0.0'
    PORT: int = 8050


settings = Settings()
app_server_settings = AppServerSettings()
