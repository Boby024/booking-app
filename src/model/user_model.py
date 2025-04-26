from ..app import db
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from ..config import Config
from sqlalchemy import text as sa_text


PASSWORD_SECRET_KEY = Config.PASSWORD_SECRET_KEY


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(512), nullable=False, unique=True)
    surname = db.Column(db.String(120), nullable=True)
    firstname = db.Column(db.String(120), nullable=True)
    description = db.Column(db.Text, nullable=True)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.DateTime, nullable=True, default=datetime.now, onupdate=datetime.now)
    access_token = db.Column(db.String(8500), nullable=True)
    roles = db.relationship('Role', secondary='user_role', lazy='subquery',
                             backref=db.backref('users', lazy=True))

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

    def get_users(self):
        return User.query.all()
    
