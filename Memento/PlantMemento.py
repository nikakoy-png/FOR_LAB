from Memento.Memento import Memento


class PlantMemento(Memento):
    def __init__(self, plant):
        self._data = plant

    def get_data(self) -> object:
        return self._data

