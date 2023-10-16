from enum import Enum

from pydantic import Field

from app.schemas.base import Base


class Question(Base):
    id_internal: int
    content: str
    answer: str
