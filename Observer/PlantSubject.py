from Factory.CreateDAOSetting import CreateDAO
from Factory.ObserverDAOCreator import ObserverDAOCreator
from MODELS.Plant import Plant
from Observer import Observer
from Observer.Subject import Subject


class PlantSubject(Subject):
    def __init__(self):
        self.__db_observer = CreateDAO(ObserverDAOCreator(), "MONGODB")
        self._observers: list[Observer] = self.__db_observer.getAllObserversPlant()
        self.plant: Plant

    def attach(self, observer) -> None:
        self._observers.append(observer)
        self.__db_observer.attach(observer)

    def detach(self, observer) -> None:
        self.__db_observer.detach(observer)
        self._observers: list[Observer] = self.__db_observer.getAllObserversPlant()

    def notify(self) -> None:
        print("Уведомляю..")
        for observer in self._observers:
            observer.update(self)

    def observer_business_logic(self, plant: Plant) -> None:
        self.plant = plant
        self.notify()

    def getPlant(self):
        return self.plant

