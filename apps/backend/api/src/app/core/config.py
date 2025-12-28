"""
Application configuration settings.
"""
import json
import os
from typing import Any

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "Backend API"
    PROJECT_DESCRIPTION: str = "FastAPI backend for the monorepo"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # CORS settings
    CORS_ORIGINS: list[str] = ["http://localhost:4200"]

    # Database settings
    DATABASE_URL: str = "mongodb://admin:admin123@localhost:27017/monorepo_db?authSource=admin"

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v: Any) -> list[str]:
        """Parse CORS_ORIGINS from string or list."""
        if isinstance(v, str):
            try:
                # Try to parse as JSON array
                return json.loads(v)
            except (json.JSONDecodeError, TypeError):
                # If not JSON, split by comma
                return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v if isinstance(v, list) else ["http://localhost:4200"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()

