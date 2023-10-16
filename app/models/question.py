from app.models.base import BaseModel
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Question(BaseModel):
    __tablename__ = "question"
    id_internal: Mapped[Integer] = mapped_column(Integer)
    content: Mapped[str] = mapped_column(String(255))
    answer: Mapped[str] = mapped_column(String(255))
