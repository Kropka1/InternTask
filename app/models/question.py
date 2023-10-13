from app.models.base import BaseModel
from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Question(BaseModel):
    __tablename__ = "question"

    question_text: Mapped[str] = mapped_column(String(255))
    question_answer: Mapped[str] = mapped_column(String(255))
