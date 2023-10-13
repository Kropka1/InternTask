from enum import Enum

from pydantic import Field

from app.schemas.base import Base


class Question(Base):
    content: str
    answer: str
