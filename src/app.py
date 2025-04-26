from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt
from .routes import register_blueprints


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # jwt = JWTManager(app)

    # Initialize extensions
    jwt.init_app(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Automatically create tables
    with app.app_context():
        # db.drop_all()
        db.create_all()

    # Register blueprints
    register_blueprints(app)

    return app
