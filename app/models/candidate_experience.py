from app.extensions import db
import uuid


class CandidateExperience(db.Model):

    __tablename__ = "candidate_experiences"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    candidate_profile_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("candidate_profiles.id"),
        nullable=False
    )

    has_prior_experience = db.Column(db.Boolean)

    industry = db.Column(db.String(150))

    years_of_experience = db.Column(db.Integer)

    specialization = db.Column(db.String(150))