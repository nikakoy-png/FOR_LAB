from MODELS.Plant import Plant
from SINGLETON.SingletonMeta import SingletonMeta


class Memory(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._mementos = []
        self._plant: Plant

    def backup(self, plant: Plant, ID_plant: int | str) -> None:
        self._mementos.append([plant.save(), ID_plant])
        self._plant = plant

    def undo(self, id_plant):
        mementos = []
        for memento_by_id in self._mementos:
            if memento_by_id[-1] == id_plant:
                mementos.append(memento_by_id)
        if not len(mementos):
            return
        memento = mementos.pop()
        self._mementos.remove(memento)
        try:
            return self._plant.restore(memento[0])
        except Exception:
            return

    def history(self):
        for memento in self._mementos:
            print(memento[0].get_data())
