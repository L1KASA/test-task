from datetime import datetime, timedelta
import pytz
from typing import Optional, List

from app.exceptions import PastReservationException, ReservationConflictException, TableNotFoundException, \
    ReservationNotFoundException
from app.repositories.reservation import ReservationRepository
from app.repositories.table import TableRepository
from app.schemas.reservation import ReservationCreate, ReservationResponse
import logging

logger = logging.getLogger(__name__)

MOSCOW_TZ = pytz.timezone('Europe/Moscow')

class ReservationService:
    def __init__(self, reservation_repo: ReservationRepository, table_repo: TableRepository):
        self.reservation_repo = reservation_repo
        self.table_repo = table_repo

    def create(self, data: ReservationCreate) -> ReservationResponse:
        logger.info(f"Creating new reservation with data: {data}")
        if not self.table_repo.exists(data.table_id):
            logger.warning(f"Table not found: {data.table_id}")
            raise TableNotFoundException(data.table_id)

        reservation_time = data.reservation_time.astimezone(MOSCOW_TZ)
        logger.debug(f"Reservation time (Moscow tz): {reservation_time}")

        if reservation_time < datetime.now(MOSCOW_TZ):
            logger.warning(f"Attempt to create reservation in the past: {reservation_time}")
            raise PastReservationException()

        if self.reservation_repo.has_conflict(
            table_id=data.table_id,
            new_start=reservation_time,
            duration=data.duration_minutes
        ):
            logger.warning(f"Reservation conflict detected for table {data.table_id} at {reservation_time}")
            raise ReservationConflictException()

        created_reservation = self.reservation_repo.create(data.model_dump())
        logger.info(f"Reservation created successfully: {created_reservation.id}")
        return created_reservation

    def get_by_id(self, reservation_id: int) -> Optional[ReservationResponse]:
        logger.debug(f"Fetching reservation by ID: {reservation_id}")
        reservation = self.reservation_repo.get_by_id(reservation_id)
        if not reservation:
            logger.warning(f"Reservation not found: {reservation_id}")
            raise ReservationNotFoundException(reservation_id)
        logger.debug(f"Found reservation: {reservation}")
        return reservation

    def get_all(self) -> List[ReservationResponse]:
        logger.debug("Fetching all reservations")
        reservations = self.reservation_repo.get_all()
        logger.debug(f"Found {len(reservations)} reservations")
        return reservations

    def delete(self, reservation_id: int) -> None:
        logger.info(f"Attempting to delete reservation: {reservation_id}")
        if not self.reservation_repo.delete(reservation_id):
            logger.warning(f"Reservation not found for deletion: {reservation_id}")
            raise ReservationNotFoundException(reservation_id)
        logger.info(f"Reservation deleted successfully: {reservation_id}")