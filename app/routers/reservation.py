from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from app.dependencies import get_reservation_service
from app.exceptions import (
    TableNotFoundException,
    ReservationConflictException,
    PastReservationException, ReservationNotFoundException
)
from app.schemas.reservation import ReservationResponse, ReservationCreate
from app.services.reservation import ReservationService

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/", response_model=list[ReservationResponse])
def get_all(service: ReservationService = Depends(get_reservation_service)):
    return service.get_all()

@router.post("/", response_model=ReservationResponse, status_code=201)
def create(
    reservation: ReservationCreate,
    service: ReservationService = Depends(get_reservation_service)
):
    try:
        return service.create(reservation)
    except TableNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    except ReservationConflictException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    except PastReservationException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)

@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_by_id(reservation_id: int, service: ReservationService = Depends(get_reservation_service)):
    try:
        return service.get_by_id(reservation_id)
    except ReservationNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)

@router.delete("/{reservation_id}", status_code=204)
def delete(reservation_id: int, service: ReservationService = Depends(get_reservation_service)):
    try:
        service.delete(reservation_id)
    except ReservationNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)