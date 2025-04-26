from flask import request
from ..extensions import jwt
from functools import wraps
from datetime import datetime
from ..model.user_model import User
from ..config import Config
from ..payload.response import response
from flask_jwt_extended import get_jwt
from sqlalchemy.exc import NoResultFound


PASSWORD_SECRET_KEY = Config.PASSWORD_SECRET_KEY
JWT_SECRET_KEY = Config.JWT_SECRET_KEY
JWT_ACCESS_TOKEN_ALGORITHM = Config.JWT_ACCESS_TOKEN_ALGORITHM
JWT_ACCESS_TOKEN_EXPIRES = Config.JWT_ACCESS_TOKEN_EXPIRES


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = None
        token = request.headers.get('Authorization')
        if not token:
            return response.response_error("Token is missing!", 401)

        try:
            # Decode the JWT token
            data = jwt.decode(token, PASSWORD_SECRET_KEY, algorithms=JWT_ACCESS_TOKEN_ALGORITHM)
            user_id = data.get('id')
            username = data.get('username')

            # Query the database for the user
            user = User.query.filter_by(id=user_id, username=username).one_or_none()
            if not user:
                return response.response_error("Invalid user!", 401)

        except jwt.ExpiredSignatureError:
            return response.response_error("Token has expired!", 401)
        except jwt.InvalidTokenError:
            return response.response_error("Invalid token!", 401)
        except NoResultFound:
            return response.response_error("User not found in the database!", 401)
    
        return f(user, *args, **kwargs)
    return decorated


def generate_token(user):
    payload = {
        "id": str(user.id),
        'username': user.username,
        'exp': datetime.utcnow() + JWT_ACCESS_TOKEN_EXPIRES,
        'roles': user.roles,
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ACCESS_TOKEN_ALGORITHM)
    return token


def roles_required(required_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            # Extract roles from the decoded JWT token
            claims = get_jwt()
            user_roles = claims.get("roles", [])

            # Check if the user has any of the required roles
            if not any(role in user_roles for role in required_roles):
                return response.response_error("Access denied! Insufficient permissions.", 403)

            return fn(*args, **kwargs)
        return decorated
    return wrapper
