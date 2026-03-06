from app.extensions import db
import uuid
from datetime import datetime


class CandidateProfile(db.Model):

    __tablename__ = "candidate_profiles"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    candidate_account_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("candidate_accounts.id"),
        nullable=False,
        unique=True
    )

    gender = db.Column(
        db.Enum("Homme", "Femme", "Autre", name="gender_enum"),
        nullable=True
    )

    birth_date = db.Column(db.Date)

    city = db.Column(db.String(100))

    country = db.Column(db.String(100))

    main_field = db.Column(db.String(150))

    short_bio = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )