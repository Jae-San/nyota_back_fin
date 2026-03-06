from app.extensions import db
import uuid
from datetime import datetime


class TestSession(db.Model):

    __tablename__ = "test_sessions"

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

    status = db.Column(db.String(50), default="in_progress")

    started_at = db.Column(db.DateTime, default=datetime.utcnow)

    completed_at = db.Column(db.DateTime)