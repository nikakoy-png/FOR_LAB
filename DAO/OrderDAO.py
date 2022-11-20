from abc import ABC, abstractmethod


class OrderDAO(ABC):
    @abstractmethod
    def makeOrder(self, ID_user: int, ID_plant: int): pass

    @abstractmethod
    def getOrderByID(self, ID: int) -> int: pass

    @abstractmethod
    def saveFunc(self): pass
