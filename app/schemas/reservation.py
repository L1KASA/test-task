# app/schemas/reservation.py
from pydantic import Field, field_validator
from .base import Base
from datetime import datetime
import pytz

class ReservationCreate(Base):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int = Field(..., gt=0)

    @field_validator('reservation_time')
    def validate_timezone(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            return pytz.timezone('Europe/Moscow').localize(v)
        return v.astimezone(pytz.timezone('Europe/Moscow'))

class ReservationResponse(ReservationCreate):
    id: int
    created_at: datetime
    updated_at: datetime