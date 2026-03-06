from app.extensions import db
import uuid
from datetime import datetime


class PersonalityTest(db.Model):

    __tablename__ = "personality_tests"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = db.Column(db.String(255), nullable=False)

    version = db.Column(db.String(50), nullable=False)

    description = db.Column(db.Text)

    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)