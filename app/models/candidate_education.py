from app.extensions import db
import uuid


class CandidateEducation(db.Model):

    __tablename__ = "candidate_educations"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    candidate_profile_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("candidate_profiles.id"),
        nullable=False
    )

    education_level = db.Column(db.String(100), nullable=False)

    institution_name = db.Column(db.String(255), nullable=False)