from fastapi import APIRouter, Depends, HTTPException

from app.exceptions import TableNotFoundException
from app.services.table import TableService
from app.schemas.table import TableCreate, TableResponse
from app.dependencies import get_table_service

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/", response_model=list[TableResponse])
def get_all(service: TableService = Depends(get_table_service)):
    return service.get_all()

@router.post("/", response_model=TableResponse, status_code=201)
def create(
    table: TableCreate,
    service: TableService = Depends(get_table_service)
):
    try:
        return service.create(table)
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

@router.get("/{table_id}", response_model=TableResponse)
def get_by_id(table_id: int, service: TableService = Depends(get_table_service)):
    try:
        return service.get_by_id(table_id)
    except TableNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)

@router.delete("/{table_id}", status_code=204)
def delete(
    table_id: int,
    service: TableService = Depends(get_table_service)
):
    try:
        service.delete(table_id)
    except TableNotFoundException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)