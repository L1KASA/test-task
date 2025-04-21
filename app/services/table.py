from app.exceptions import TableNotFoundException
from app.repositories.table import TableRepository
from app.schemas.table import TableCreate, TableResponse
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class TableService:
    def __init__(self, repo: TableRepository):
        self.repo = repo

    def create(self, data: TableCreate) -> TableResponse:
        logger.info(f"Creating new table with data: {data}")
        created_table = self.repo.create(data.model_dump())
        logger.info(f"Created table with ID {created_table.id}")
        return created_table

    def get_by_id(self, table_id: int) -> Optional[TableResponse]:
        logger.debug(f"Fetching table by ID: {table_id}")
        table = self.repo.get_by_id(table_id)
        if not table:
            logger.warning(f"Table with ID {table_id} not found")
            raise TableNotFoundException(table_id)
        logger.debug(f"Found table: {table}")
        return table

    def get_all(self) -> List[TableResponse]:
        logger.debug("Fetching all tables")
        tables = self.repo.get_all()
        logger.debug(f"Found {len(tables)} tables")
        return tables

    def delete(self, table_id: int) -> None:
        logger.info(f"Deleting table with ID {table_id}")
        deleted_table = self.repo.delete(table_id)
        if not deleted_table:
            logger.warning(f"Table with ID {table_id} not found, cannot delete")
            raise TableNotFoundException(table_id)
        logger.info(f"Deleted table with ID {table_id}")