from dotenv import load_dotenv
import os
from .utils.log import Logger
from datetime import datetime, timedelta


load_dotenv()
log_path = f"src/logs/app_{datetime.now().strftime('%Y%m%d')}.log"
logger = Logger(name=__name__, log_file=log_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = os.getenv('ENV').lower()

    if os.getenv('ENV') == "dev":
        DEBUG = True
        SQLALCHEMY_ECHO = True
        SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')
        PASSWORD_SECRET_KEY = os.getenv('PASSWORD_SECRET_KEY_DEV')
        JWT_SECRET_KEY = os.getenv('JWT_TOKEN_SECRET_DEV')
        JWT_ACCESS_TOKEN_ALGORITHM = ["HS256"]
        JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=6)

    elif os.getenv('ENV') == "prod":
        DEBUG = False
        SQLALCHEMY_ECHO = False
        SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_PROD')
        PASSWORD_SECRET_KEY = os.getenv('PASSWORD_SECRET_KEY_PROD')
        JWT_SECRET_KEY = os.getenv('JWT_TOKEN_SECRET_PROD')
        JWT_ACCESS_TOKEN_ALGORITHM = ["HS256"]
        JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=3)
    
    logger.info(f"{ENV} SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI}")
    logger.info(f"{ENV} JWT_TOKEN_SECRET: {JWT_SECRET_KEY}")
    logger.info(f"{ENV} JWT_ACCESS_TOKEN_EXPIRES: {JWT_ACCESS_TOKEN_EXPIRES}")
    logger.info(f"{ENV} JWT_ACCESS_TOKEN_EXPIRES: {PASSWORD_SECRET_KEY}")
