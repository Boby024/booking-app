from dotenv import load_dotenv
import os
from .utils.log import Logger
from datetime import datetime, timedelta
from .utils import helper


load_dotenv()
log_path = f"src/logs/app_{datetime.now().strftime('%Y%m%d')}.log"
logger = Logger(name=__name__, log_file=log_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = os.getenv('ENV').upper()
    DEBUG = True if ENV == "DEV" else False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = os.getenv(f'SQLALCHEMY_DATABASE_URI_{ENV}')
    SECRET_KEY = os.getenv(f'SECRET_KEY{ENV}')
    PASSWORD_SECRET_KEY = os.getenv(f'PASSWORD_SECRET_KEY_{ENV}')
    JWT_SECRET_KEY = os.getenv(f'JWT_TOKEN_SECRET_{ENV}')
    JWT_ACCESS_TOKEN_ALGORITHM = ["HS256"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=6) if ENV == "DEV" else timedelta(hours=3)
    FLASK_THREADED = True if os.getenv(f'FLASK_THREADED_{ENV}').lower() == "true" else False
    FLASK_PORT = int(os.getenv(f'FLASK_PORT_{ENV}')) if os.getenv(f'FLASK_PORT_{ENV}') else 5000
    FLASK_HOST = os.getenv(f'FLASK_HOST_{ENV}') if os.getenv(f'FLASK_HOST_{ENV}') else "localhost"

    LOGS_PATH = os.getenv('LOGS_PATH')
    # log_path = f"{LOGS_PATH}/app_{datetime.now().strftime('%Y%m%d')}.log"
    log_path = f"{LOGS_PATH}/app_{helper.get_dt_utcnow().strftime('%Y%m%d')}.log"

    MAIL_SERVER = os.getenv(f'MAIL_SERVER_{ENV}')
    MAIL_PORT = int(os.getenv(f'MAIL_PORT_{ENV}')) if os.getenv(f'MAIL_PORT_{ENV}') else 587
    MAIL_USE_TLS = True if os.getenv(f'MAIL_USE_TLS_{ENV}').lower() == "true" else False
    MAIL_USERNAME = os.getenv(f'MAIL_USERNAME_{ENV}')
    MAIL_PASSWORD = os.getenv(f'MAIL_USERNAME_{ENV}')
    MAIL_EMAIL_VERIFICATION_SUBJECT = os.getenv(f'MAIL_EMAIL_VERIFICATION_SUBJECT_{ENV}')
    MAIL_EMAIL_VERIFICATION_CONTENT = os.getenv(f'MAIL_EMAIL_VERIFICATION_CONTENT_{ENV}')
    MAIL_EMAIL_VERIFICATION_CONTENT_PATH_DEV = os.getenv(f'MAIL_EMAIL_VERIFICATION_CONTENT_PATH_{ENV}')

    # if ENV == "DEV":
    logger.info(f"ENV {ENV}")
    logger.info(f"log_path {log_path}")
    logger.info(f"SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI}")
    logger.info(f"JWT_TOKEN_SECRET: {JWT_SECRET_KEY}")
    logger.info(f"JWT_ACCESS_TOKEN_EXPIRES: {JWT_ACCESS_TOKEN_EXPIRES}")
    logger.info(f"JWT_ACCESS_TOKEN_EXPIRES: {PASSWORD_SECRET_KEY}")
    
    logger.info(f"FLASK_THREADED {FLASK_THREADED} AND {type(FLASK_THREADED)}")
    logger.info(f"HOST {FLASK_HOST}")
    logger.info(f"PORT {FLASK_PORT}")
