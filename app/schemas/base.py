from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel):
    id: int
    create_time: datetime
