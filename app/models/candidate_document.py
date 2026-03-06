from app.extensions import db
import uuid
from datetime import datetime


class CandidateDocument(db.Model):

    __tablename__ = "candidate_documents"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    candidate_profile_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("candidate_profiles.id"),
        nullable=False
    )

    document_type = db.Column(
        db.String(50),
        nullable=False
    )

    file_name = db.Column(
        db.String(255),
        nullable=False
    )

    storage_path = db.Column(
        db.String(500),
        nullable=False
    )

    file_size_bytes = db.Column(
        db.Integer
    )

    mime_type = db.Column(
        db.String(100)
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )