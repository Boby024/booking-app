from ..extensions import db
from sqlalchemy.dialects.postgresql import UUID


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Direct relationship to UserRole for accessing users indirectly
    user_roles = db.relationship('UserRole', back_populates='role', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
    

class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'), nullable=False)
    
    # Relationships to User and Role
    user = db.relationship('User', back_populates='user_roles')
    role = db.relationship('Role', back_populates='user_roles')
