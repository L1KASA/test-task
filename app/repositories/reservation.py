from datetime import datetime, timedelta
from sqlalchemy import and_, exists, text
from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from app.repositories.base import BaseRepository


class ReservationRepository(BaseRepository[Reservation]):
    def __init__(self, db: Session):
        super().__init__(Reservation, db)

    def _get_time_conflict_condition(
            self,
            table_id: int,
            new_start: datetime,
            new_end: datetime
    ):
        return and_(
            self.model.table_id == table_id,
            self.model.reservation_time < new_end,
            self.model.reservation_time + (self.model.duration_minutes * text("INTERVAL '1 minute'")) > new_start
        )

    def has_conflict(
            self,
            table_id: int,
            new_start: datetime,
            duration: int
    ) -> bool:
        new_end = new_start + timedelta(minutes=duration)

        conflict_condition = self._get_time_conflict_condition(table_id, new_start, new_end)

        return self.db.query(exists().where(conflict_condition)).scalar()