import pymongo
from pymongo import errors
from SINGLETON.SingletonMeta import SingletonMeta


class NoSQL(metaclass=SingletonMeta):
    def __init__(self):
        try:
            self.db_client = pymongo.MongoClient('mongodb://localhost:27017')
            self.current_db = self.db_client['For_lab_NSOL']
            self.collection_plant = self.current_db[f'Plant']
            self.collection_user = self.current_db[f'User']
            self.collection_order = self.current_db[f'Order']
            self.collection_observer = self.current_db[f'Observer']
        except errors as e:
            print(f'FATAL ERROR WITH CONNECT MONGODB: {e}')
            
