from datetime import datetime

from bson import ObjectId

from DAO.OrderDAO import OrderDAO
from DB.NoSQL import NoSQL
from MODELS.Order import Order


class OrderDAONoSQL(OrderDAO):
    def __init__(self):
        self.nosql = NoSQL().collection_order

    def makeOrder(self, ID_user: str, ID_plant: str):
        if NoSQL().collection_plant.find_one({'_id': ObjectId(ID_plant)}) is None:
            print('+')
            return None
        request = {
            'user_id': ID_user,
            'plant_id': ID_plant,
            'date_of_make': str(datetime.today()).split()[0],
        }
        self.nosql.insert_one(request)

    def getOrderByID(self, ID: str) -> Order:
        order = None
        try:
            result = self.nosql.find_one({'_id': ObjectId(ID)})
            order = Order.OrderBuilder() \
                .IdOrder(str(result['_id'])) \
                .UserID('user_id') \
                .PlantID(str(result['plant_id'])) \
                .Date(str(result['date_of_make'])) \
                .build()
        except Exception as e:
            print(f'FATAL ERROR {e}')
        return order

    def saveFunc(self):
        pass
