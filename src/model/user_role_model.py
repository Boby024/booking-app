from ..app import db
from sqlalchemy.dialects.postgresql import UUID


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)  # UUID as foreign key
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    # Relationships for easier access
    user = db.relationship('User', backref=db.backref('user_roles', lazy=True))
    role = db.relationship('Role', backref=db.backref('role_users', lazy=True))

