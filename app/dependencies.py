from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.reservation import ReservationRepository
from app.services.table import TableService
from app.services.reservation import ReservationService
from app.repositories.table import TableRepository
from app.database import get_db


def get_db_session(db: Session = Depends(get_db)):
    return db

def get_table_service(db: Session = Depends(get_db)) -> TableService:
    repo = TableRepository(db)
    return TableService(repo)

def get_reservation_service(db: Session = Depends(get_db)) -> ReservationService:
    resrvation_repo = ReservationRepository(db)
    table_repo = TableRepository(db)
    return ReservationService(resrvation_repo, table_repo)