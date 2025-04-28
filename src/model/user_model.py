from ..extensions import db
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from ..config import Config
from ..utils import helper
from sqlalchemy import text as sa_text
from ..model.access_token_model import AccessToken
from ..model.user_role_model import Role, UserRole
from ..model.email_verification_model import EmailVerification


PASSWORD_SECRET_KEY = Config.PASSWORD_SECRET_KEY

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    surname = db.Column(db.String(120), nullable=True)
    firstname = db.Column(db.String(120), nullable=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=helper.get_dt_utcnow())
    updated_at = db.Column(db.DateTime, nullable=True) # , default=datetime.now, onupdate=datetime.now)
    is_email_verified = db.Column(db.Boolean, default=False, nullable=False)
    # One-to-Many Relationship with AccessToken
    access_tokens = db.relationship('AccessToken', back_populates='user', lazy=True, cascade="all, delete-orphan")
    email_verifications = db.relationship('EmailVerification', back_populates='user', lazy=True, cascade="all, delete-orphan")
    # Relationship to UserRole
    user_roles = db.relationship('UserRole', back_populates='user', lazy=True)


    def set_password(self, plaintext_password):
        salted_password = plaintext_password + PASSWORD_SECRET_KEY  # Add secret key to password
        self.password = generate_password_hash(salted_password)

    def verify_password(self, plaintext_password):
        salted_password = plaintext_password + PASSWORD_SECRET_KEY  # Add secret key to password
        return check_password_hash(self.password, salted_password)

    def serialize(self):
        return {
            "id": str(self.id),
            "email": self.email,
            "surname": self.surname,
            "firstname": self.firstname,
        }

    # def get_users(self):
    #     return User.query.all()
