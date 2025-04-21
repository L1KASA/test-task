from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

from .base import Base
class Table(Base):

    name: Mapped[str] = mapped_column(String(50), unique=True)
    seats: Mapped[int] = mapped_column(Integer)
    location: Mapped[str] = mapped_column(String(50))