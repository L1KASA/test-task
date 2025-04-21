from typing import List, Optional

from sqlalchemy.orm import DeclarativeBase, Session
from typing_extensions import TypeVar, Generic

from app.repositories.abstract_base import AbstractBaseRepository

T = TypeVar("T", bound=DeclarativeBase)


class BaseRepository(AbstractBaseRepository, Generic[T]):
    def __init__(self, model: type[T], db: Session):
        self.db = db
        self.model = model

    def get_all(self) -> List[T]:
        return self.db.query(self.model).all()

    def get_by_id(self, id: int) -> Optional[T]:
        return self.db.query(self.model).filter_by(id=id).first()

    def create(self, data: dict) -> T:
        instance = self.model(**data)
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def delete(self, id: int) -> Optional[T]:
        try:
            instance = self.db.get(self.model, id)
            if instance:
                self.db.delete(instance)
                self.db.commit()
                return instance
            return None
        except Exception as e:
            self.db.rollback()
            raise ValueError(f"Delete error: {str(e)}")