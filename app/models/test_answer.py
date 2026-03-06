from app.extensions import db
import uuid


class TestAnswer(db.Model):

    __tablename__ = "test_answers"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    test_session_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("test_sessions.id"),
        nullable=False
    )

    test_question_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("test_questions.id"),
        nullable=False
    )

    answer_option_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("answer_options.id"),
        nullable=True
    )

    score = db.Column(db.Integer, nullable=True)