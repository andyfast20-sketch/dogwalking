import os
from pathlib import Path


class Config:
    """Base configuration for the Dogwalking web application."""

    BASE_DIR = Path(__file__).resolve().parent
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///" + str(BASE_DIR / "instance" / "dogwalking.sqlite3"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SITE_BASE_URL = os.getenv(
        "SITE_BASE_URL", "https://dogwalking-opxq.onrender.com"
    ).rstrip("/")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
