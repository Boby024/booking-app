from ..extensions import db
from sqlalchemy.dialects.postgresql import UUID
from ..utils import helper


class AccessToken(db.Model):
    __tablename__ = 'access_token'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)  # Foreign key to User table
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    token = db.Column(db.String(512), nullable=False)
    refresh_token = db.Column(db.String(512), nullable=True)
    revoked = db.Column(db.Boolean, default=False, nullable=False)
    ip_address = db.Column(db.String(45), nullable=True)  # Optional, for tracking
    device_info = db.Column(db.Text, nullable=True)  # Optional, for additional details
    created_at  = db.Column(db.DateTime, nullable=False) # When it was issued
    expires_at = db.Column(db.DateTime, nullable=False) # When the access token expires
    updated_at = db.Column(db.DateTime, nullable=True)

    # Relationship to User
    user = db.relationship('User', back_populates='access_tokens')

    def __repr__(self):
        return f"<AccessToken id={self.id} user_id={self.user_id}>"

    def is_expired(self):
        """Check if the token has expired."""
        return helper.get_dt_utcnow() > self.expires_at

    def revoke(self):
        """Revoke the access token."""
        self.revoked = True
        db.session.commit()
