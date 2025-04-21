from flask import Flask
from .config import DevConfig
from .extensions import db, migrate
from .routes import register_blueprints

def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    register_blueprints(app)

    return app
