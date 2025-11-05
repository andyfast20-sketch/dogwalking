import os
from pathlib import Path
from typing import Final


def _normalize_database_url(value: str) -> str:
    """Render.com uses postgres://, which SQLAlchemy 2 rejects."""

    if value.startswith("postgres://"):
        return "postgresql://" + value.removeprefix("postgres://")
    return value


class Config:
    """Base configuration for the Dogwalking web application."""

    BASE_DIR: Final[Path] = Path(__file__).resolve().parent
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    SQLALCHEMY_DATABASE_URI = _normalize_database_url(
        os.getenv(
            "DATABASE_URL",
            "sqlite:///" + str(BASE_DIR / "instance" / "dogwalking.sqlite3"),
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SITE_BASE_URL = os.getenv(
        "SITE_BASE_URL", "https://dogwalking-opxq.onrender.com"
    ).rstrip("/")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
