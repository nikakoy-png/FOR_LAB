import logging as lg

from Memento.Memento import Memento
from Memento.PlantMemento import PlantMemento


class Plant(object):
    def __init__(self, plantbuild):
        self.__variety = plantbuild._variety
        self.__price = plantbuild._price
        self.__growth = plantbuild._growth
        self.__sun_loving = plantbuild._sun_loving
        self.__description = plantbuild._description
        self.__prolific = plantbuild._prolific

    @property
    def getVariety(self) -> str:
        return self.__variety

    @property
    def getPrice(self) -> float or int:
        return self.__price

    @property
    def getGrowth(self) -> float or int:
        return self.__growth

    @property
    def getSun_loving(self) -> bool:
        return self.__sun_loving

    @property
    def getDescription(self) -> str:
        return self.__description

    @property
    def getProlific(self) -> bool:
        return self.__prolific

    def setVariety(self, variety):
        try:
            if type(variety) != str:
                raise TypeError
            self.__variety = variety
        except TypeError:
            lg.error('Type Error')

    def setPrice(self, price):
        try:
            if type(price) != float or int:
                raise TypeError
            self.__price = price
        except TypeError:
            lg.error('Type Error')

    def setGrowth(self, growth):
        try:
            if type(growth) != float or int:
                raise TypeError
            self.__growth = growth
        except TypeError:
            lg.error('Type Error')

    def setSun_loving(self, sun_loving):
        try:
            if type(sun_loving) != bool:
                raise TypeError
            self.__sun_loving = sun_loving
        except TypeError:
            lg.error('Type Error')

    def setDescription(self, description):
        try:
            if type(description) != str:
                raise TypeError
            self.__description = description
        except TypeError:
            lg.error('Type Error')

    def setProlific(self, prolific):
        try:
            if type(prolific) != bool:
                raise TypeError
            self.__prolific = prolific
        except TypeError:
            lg.error('Type Error')

    def __str__(self) -> str:
        return f'*********************************\n' \
               f'Price:{self.__price}\n' \
               f'Growth:{self.__growth}\n' \
               f'Variety:{self.__variety}\n' \
               f'Description:{self.__description}\n' \
               f'Prolific:{self.__prolific}\n' \
               f'Sun_loving:{self.__sun_loving}\n' \
               f'*********************************'

    def save(self) -> Memento:
        return PlantMemento(self)

    def restore(self, memento: Memento):
        r_plant = memento.get_data()
        self.__growth = r_plant.getGrowth
        self.__price = r_plant.getPrice
        self.__variety = r_plant.getVariety
        self.__prolific = r_plant.getProlific
        self.__description = r_plant.getDescription
        self.__sun_loving = r_plant.getSun_loving
        return self

    class PlantBuilder:
        def __init__(self):
            self._variety = str
            self._price = float | int
            self._growth = float | int
            self._sun_loving = bool
            self._description = str
            self._prolific = bool

        def Variety(self, Variety: str):
            self._variety = Variety
            return self

        def Price(self, Price: float | int):
            self._price = Price
            return self

        def Growth(self, Growth: float | int):
            self._growth = Growth
            return self

        def Sun_loving(self, Sun_Loving: bool):
            if Sun_Loving:
                self._sun_loving = 1
            else:
                self._sun_loving = 0
            return self

        def Description(self, Description: str):
            self._description = Description
            return self

        def Prolific(self, Prolific: bool):
            if Prolific:
                self._prolific = 1
            else:
                self._prolific = 0
            return self

        def build(self):
            return Plant(self)
