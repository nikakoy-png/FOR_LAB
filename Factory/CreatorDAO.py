from abc import ABC, abstractmethod


class CreatorDAO(ABC):
    @abstractmethod
    def factory_method(self, type_db: str): pass

    def operation_create_object(self, type_db: str):
        return self.factory_method(type_db)
