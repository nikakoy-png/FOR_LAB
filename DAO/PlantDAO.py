from abc import ABC, abstractmethod
from MODELS import Plant


class PlantDAO(ABC):
    @abstractmethod
    def getAllPlantsByUser(self, ID_user: int) -> list: pass

    @abstractmethod
    def getPlantByID(self, ID: int) -> Plant: pass

    @abstractmethod
    def getPlantByMAXPrice(self) -> list or Plant: pass

    @abstractmethod
    def getPlantByMINPrice(self) -> list or Plant: pass

    @abstractmethod
    def delPlant(self, ID: int): pass

    @abstractmethod
    def updatePlant(self, plant: Plant, ID: int): pass

    @abstractmethod
    def addNewPlant(self, plant: Plant): pass
