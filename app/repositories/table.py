from sqlalchemy import select, exists
from sqlalchemy.orm import Session

from app.models.table import Table
from app.repositories.base import BaseRepository

class TableRepository(BaseRepository[Table]):
    def __init__(self, db: Session):
        super().__init__(model=Table, db=db)

    def exists(self, table_id: int) -> bool:
        stmt = select(exists().where(self.model.id == table_id))
        return self.db.execute(stmt).scalar()