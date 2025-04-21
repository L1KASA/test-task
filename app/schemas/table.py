from datetime import datetime
from .base import Base

class TableCreate(Base):
    name: str
    seats: int
    location: str

class TableResponse(TableCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True