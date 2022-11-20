from abc import ABC, abstractmethod


class Memento(ABC):
    @abstractmethod
    def get_data(self): pass
