from ..extensions import db
from sqlalchemy.dialects.postgresql import UUID
from ..utils import helper


class EmailVerification(db.Model):
    __tablename__ = 'email_verification'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    code = db.Column(db.String(10), nullable=False)  # Verification code, alphanumeric
    created_at = db.Column(db.DateTime, default=helper.get_dt_utcnow(), nullable=False)  # Creation timestamp
    expires_at = db.Column(db.DateTime, nullable=False)  # Expiration timestamp
    verified = db.Column(db.Boolean, default=False, nullable=False)  # Tracks whether the code is verified

    # Relationship back to User
    user = db.relationship('User', back_populates='email_verifications')
