from datetime import datetime
from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

# Initialize extensions without app; they can be bound in create_app

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()


def create_app(config_object: str | None = None) -> Flask:
    """Application factory for the Dogwalker site."""

    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder="static",
        template_folder="templates",
    )

    config_path = config_object or "config.Config"
    app.config.from_object(config_path)

    instance_dir = Path(app.instance_path)
    instance_dir.mkdir(parents=True, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    @app.context_processor
    def inject_globals():  # pragma: no cover - context injection
        return {"current_year": datetime.utcnow().year}

    from . import models  # noqa: F401
    from .routes import main

    app.register_blueprint(main)

    return app
