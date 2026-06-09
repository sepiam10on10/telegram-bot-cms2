# ==========================================
# CONFIG MODULE - SETTINGS MANAGEMENT
# PURPOSE: Centralized configuration for all environments
# ==========================================

from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    """
    ==========================================
    APPLICATION SETTINGS
    PURPOSE: Store and manage configuration
    ==========================================
    """

    # ==========================================
    # API CONFIGURATION
    # ==========================================
    API_TITLE: str = "Telegram Bot CMS"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "Dynamic Telegram Bot Management System"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = True

    # ==========================================
    # TELEGRAM CONFIGURATION
    # ==========================================
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_BOT_USERNAME: str

    # ==========================================
    # DATABASE CONFIGURATION
    # ==========================================
    DATABASE_URL: str = "sqlite:///./app.db"
    SQLALCHEMY_ECHO: bool = False

    # ==========================================
    # JWT & SECURITY CONFIGURATION
    # ==========================================
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ==========================================
    # ADMIN CONFIGURATION
    # ==========================================
    ADMIN_USERNAME: str = "admin"
    ADMIN_EMAIL: str = "admin@example.com"
    ADMIN_PASSWORD: str

    # ==========================================
    # REDIS CONFIGURATION
    # ==========================================
    REDIS_URL: str = "redis://localhost:6379/0"

    # ==========================================
    # CORS CONFIGURATION
    # ==========================================
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]

    # ==========================================
    # LOGGING CONFIGURATION
    # ==========================================
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    # ==========================================
    # SMTP CONFIGURATION (for email notifications)
    # ==========================================
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_EMAIL: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = True


# ==========================================
# SINGLETON SETTINGS INSTANCE
# PURPOSE: Global configuration access
# ==========================================
settings = Settings()
