from app.extensions import db
import uuid


class TestQuestion(db.Model):

    __tablename__ = "test_questions"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    personality_test_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("personality_tests.id"),
        nullable=False
    )

    question_text = db.Column(db.Text, nullable=False)

    step = db.Column(db.Integer, nullable=False)

    order_index = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime)