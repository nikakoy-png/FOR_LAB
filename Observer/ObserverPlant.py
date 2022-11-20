from email.mime.multipart import MIMEMultipart

from Observer.Observer import Observer
import smtplib
from Observer.Subject import Subject


class ObserverPlant(Observer):
    def __init__(self, ObserverPlantBuilder):
        self.__email: str = ObserverPlantBuilder._email
        self.__name: str = ObserverPlantBuilder._name
        self.__plant_variety: str = ObserverPlantBuilder._plant_variety
        self.__price: int | float = ObserverPlantBuilder._price

    def getEmail(self):
        return self.__email

    def getName(self):
        return self.__name

    def getPlantVariety(self):
        return self.__plant_variety

    def getPrice(self):
        return self.__price

    def update(self, subject):
        if int(subject.getPlant().getPrice) == int(
                self.__price) and subject.getPlant().getVariety == self.__plant_variety:
            print(f'User {self.__name} Notify!')

    class ObserverPlantBuilder:
        def __init__(self):
            self._email = str
            self._name = str
            self._plant_variety = str
            self._price = float | int

        def Email(self, Email: str):
            self._email = Email
            return self

        def Price(self, Price: float | int):
            self._price = Price
            return self

        def PlantVariety(self, PlantVariety: str):
            self._plant_variety = PlantVariety
            return self

        def Name(self, Name: str):
            self._name = Name
            return self

        def build(self):
            return ObserverPlant(self)
