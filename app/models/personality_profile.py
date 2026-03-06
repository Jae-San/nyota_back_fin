from app.extensions import db
import uuid
from datetime import datetime


class PersonalityProfile(db.Model):

    __tablename__ = "personality_profiles"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    candidate_profile_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("candidate_profiles.id"),
        nullable=False
    )

    personality_test_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("personality_tests.id"),
        nullable=False
    )

    ouverture_curiosite = db.Column(db.Integer)

    discipline_fiabilite = db.Column(db.Integer)

    influence_presence = db.Column(db.Integer)

    cooperation = db.Column(db.Integer)

    resilience_stress = db.Column(db.Integer)

    drive_motivation = db.Column(db.Integer)

    style_action = db.Column(db.Integer)

    alignement_strategique = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)