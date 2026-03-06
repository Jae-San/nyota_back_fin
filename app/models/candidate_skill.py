from app.extensions import db
import uuid
from datetime import date


class CandidateSkill(db.Model):

    __tablename__ = "candidate_skills"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    candidate_profile_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("candidate_profiles.id"),
        nullable=False
    )

    target_industry = db.Column(db.String(150))

    languages = db.Column(db.String(255))

    target_job_title = db.Column(db.String(150))

    target_job_level = db.Column(db.String(100))

    expected_salary_min = db.Column(db.Integer)

    work_mode = db.Column(db.String(50))

    open_to_relocation = db.Column(db.Boolean)

    current_location = db.Column(db.String(150))

    nationality = db.Column(db.String(100))

    availability_date = db.Column(db.Date)