from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, TIMESTAMP

from .base import Base
class Reservation(Base):
    customer_name: Mapped[str] = mapped_column(String(50))
    table_id: Mapped[int] = mapped_column(ForeignKey('tables.id'))
    reservation_time: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
    duration_minutes: Mapped[int]

