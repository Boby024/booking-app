from flask import Blueprint, request
from ..service import user_service
from ..utils.auth_security import token_required, roles_required
from src.payload.request.user_request import UserRegisterRequest, UserLoginRequest
from ..payload.response import response
from ..utils.log import Logger
from src.config import Config


user_bp = Blueprint("user", __name__)
logger = Logger(name=__name__, log_file=Config.log_path)


@user_bp.route('/register', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        urr = UserRegisterRequest(**data)
        user_created = user_service.register(urr)
        if user_created is not None:
            return response.response_data(user_created, 201)
        else:
            response.response_error("Invalid credentials! Or Email already used", 400)
    except Exception as e:
        return response.response_error("Missing Attributes: username, password, email, firstname, lastname", 400)


@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        ulr = UserLoginRequest(**data)
        token = user_service.login(ulr)
        if token:
            return response.response_data({"token": token}, 200)
        else:
            return response.response_error("Invalid credentials!", 400)
        
    except Exception as e:
        return response.response_error("Missing username or password!", 400)


@user_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = user_service.get_users()
        return response.response_data(data=users, code=200, serialized=True)
    except Exception as e:
        return response.response_error("Internal Server Error", 500)


@user_bp.route('/roles', methods=['GET'])
def get_roles():
    try:
        roles = user_service.get_roles()
        return response.response_data(data=roles, code=200, serialized=True)
    except Exception as e:
        return response.response_error("Internal Server Error!", 500)


@user_bp.route('/block', methods=['GET'])
@token_required
@roles_required(['ADMIN', 'MANAGER']) 
def test(user):
    logger.info("current user")
    print(user.__dict__)
    return response.response_data({"user": "works"}, 201)
