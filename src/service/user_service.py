from src.payload.request.user_request import UserRegisterRequest, UserLoginRequest
from src.model.user_model import User
from ..app import db
from ..utils.auth_security import generate_token
from ..utils.log import Logger
from datetime import datetime
from ..model.user_role_model import Role, UserRole


log_path = f"src/logs/app_{datetime.now().strftime('%Y%m%d')}.log"
logger = Logger(name=__name__, log_file=log_path)


def register(data: UserRegisterRequest):
    roles = data.roles  # List of role names
    role_objects = Role.query.filter(Role.name.in_(roles)).all()
    urr_dict = data.register_dict()

    new_user = User(**urr_dict)
    new_user.set_password(data.password)
    db.session.add(new_user)
    db.session.commit()

    # Create UserRole entries
    for role in role_objects:
        user_role = UserRole(user_id=new_user.id, role_id=role.id)
        db.session.add(user_role)

    return new_user.to_dict()


def login(data: UserLoginRequest):
    user = User.query.filter_by(username=data.username).first()
    token = None

    # Validate password using secret key
    if user and user.verify_password(data.password): 
        token = generate_token(user=user)
        return token
    return None


def add_role(data):
    pass


def get_users():
    return User.query.all()

