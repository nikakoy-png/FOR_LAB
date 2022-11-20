from abc import ABC, abstractmethod

from Observer.Subject import Subject


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject): pass
