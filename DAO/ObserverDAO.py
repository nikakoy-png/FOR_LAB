from abc import ABC, abstractmethod



class ObserverDAO(ABC):
    @abstractmethod
    def attach(self, observer) -> None: pass

    @abstractmethod
    def detach(self, ID) -> None: pass

    @abstractmethod
    def getAllObserversPlant(self) -> list: pass
