class Order(object):
    def __init__(self, orderbuild):
        self.__id_order = orderbuild._id_order
        self.__date = orderbuild._date
        self.__plant_id = orderbuild._plant_id
        self.__user_id = orderbuild._user_id

    @property
    def getIdOrder(self) -> str:
        return self.__id_order

    @property
    def getDate(self) -> str:
        return self.__date

    @property
    def getPlantID(self) -> str:
        return self.__plant_id

    @property
    def getUserID(self) -> str:
        return self.__user_id

    def __str__(self):
        return (f'*****************************\n'
                f'id_order: {self.__id_order}\n'
                f'date: {self.__date}\n'
                f'plant_id: {self.__plant_id}\n'
                f'user_id: {self.__user_id}\n'
                f'*****************************\n')

    class OrderBuilder:
        def __init__(self):
            self._id_order = str
            self._date = str
            self._plant_id = str
            self._user_id = str

        def IdOrder(self, IdOrder: str):
            self._id_order = IdOrder
            return self

        def Date(self, Date: str):
            self._date = Date
            return self

        def PlantID(self, PlantID: str):
            self._plant_id = PlantID
            return self

        def UserID(self, UserID: str):
            self._user_id = UserID
            return self

        def build(self):
            return Order(self)


