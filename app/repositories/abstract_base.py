from abc import ABC, abstractmethod

class AbstractBaseRepository(ABC):
    @abstractmethod
    def get_all(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def create(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, **kwargs):
        raise NotImplementedError
