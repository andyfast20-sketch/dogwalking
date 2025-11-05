from pathlib import Path


class Config:
    """Base configuration for the Dogwalking web application."""

    BASE_DIR = Path(__file__).resolve().parent
    SECRET_KEY = "change-me"
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + str(BASE_DIR / "instance" / "dogwalking.sqlite3")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
