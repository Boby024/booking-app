from src.payload.request.user_request import UserRegisterRequest, UserLoginRequest
from src.model.user_model import User
from ..app import db
from ..utils.auth_security import generate_token
from ..utils.log import Logger
from src.config import Config
from flask_mail import Message
from ..extensions import mail
from ..utils import helper
from ..model.user_role_model import Role, UserRole
from ..model.access_token_model import AccessToken
from ..model.email_verification_model import EmailVerification


logger = Logger(name=__name__, log_file=Config.log_path)


def send_email_verification(receiver, name):
    email_verification_code = helper.generate_verification_code(10)
    subject = Config.MAIL_EMAIL_VERIFICATION_SUBJECT
    sender = Config.MAIL_USERNAME
    # content = Config.MAIL_EMAIL_VERIFICATION_CONTENT
    content = content = helper.read_file(Config.MAIL_EMAIL_VERIFICATION_CONTENT_PATH_DEV)
    receiver = str(receiver).strip()
    body = content.replace("sender_info_surname", name).replace("email_verification_code", email_verification_code)
    status = False
    try:
        msg = Message(subject=subject,
                    sender=sender,
                    recipients=[receiver])
        msg.body = body
        mail.send(msg)
    except Exception as e:
        pass

    if status:
        return True
    return False


def register(data: UserRegisterRequest):
    # check if email not exist
    user_found = User.query.filter_by(email=data.email).first()
    if user_found is None:
        return None

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
    
    # Send verification mail
    send_email_verification(receiver=new_user.email, name=new_user.firstname)
    return new_user.serialize()


def login(data: UserLoginRequest):
    user = User.query.filter_by(email=data.email).first()
    token = None

    # Validate password using secret key
    if user and user.verify_password(data.password): 
        token = generate_token(user=user)
        return token
    return None


def verify_email(data):
    email = data["email"]
    code = data["code"]
    user = User.query.filter_by(email=data.email).first()
    if user:
        email_verifications = EmailVerification.query.filter_by(email=email).first()
        pass


def test():
    # return Role.query.all()
    # return UserRole.query.all()
    return AccessToken.query.all()


def get_users():
    return User.query.all()


def get_roles():
    return Role.query.all()
