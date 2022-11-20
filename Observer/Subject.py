from abc import ABC, abstractmethod


class Subject(ABC):
    """
    Интферфейс издателя объявляет набор методов для управлениями подписчиками.
    """
    @abstractmethod
    def attach(self, observer) -> None: pass
    @abstractmethod
    def detach(self, observer) -> None: pass
    @abstractmethod
    def notify(self) -> None: pass
