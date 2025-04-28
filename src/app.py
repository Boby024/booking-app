from flask import Flask
# from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, jwt, mail
from .routes import register_blueprints


def create_app(config_class=Config):
    app = Flask(__name__)
    # cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(config_class)

    # Initialize extensions
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Automatically create tables
    with app.app_context():
        # db.drop_all()
        db.create_all()

    # Register blueprints
    register_blueprints(app)

    return app
