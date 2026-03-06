from app.extensions import db
import uuid


class AnswerOption(db.Model):

    __tablename__ = "answer_options"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    test_question_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("test_questions.id"),
        nullable=False
    )

    label = db.Column(db.String(255), nullable=False)

    score_value = db.Column(db.Integer, nullable=False)

    order_index = db.Column(db.Integer, nullable=False)