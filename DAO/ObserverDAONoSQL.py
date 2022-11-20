from datetime import datetime

from bson import ObjectId

from DAO.ObserverDAO import ObserverDAO
from DB.NoSQL import NoSQL
from Observer.ObserverPlant import ObserverPlant


class ObserverDAONoSQL(ObserverDAO):
    def __init__(self):
        self.nosql = NoSQL().collection_observer

    def attach(self, observer: ObserverPlant) -> None:
        request = {
            'variety': observer.getPlantVariety(),
            'price': observer.getPrice(),
            'name': observer.getName(),
            'email': observer.getEmail(),
            'date_of_creation': str(datetime.today()).split()[0]
        }
        print(request)
        self.nosql.insert_one(request)

    def detach(self, ID) -> None:
        self.nosql.delete_one({'_id': ObjectId(ID)})

    def getAllObserversPlant(self) -> list[ObserverPlant]:
        observer = []
        for x in self.nosql.find({}):
            observer.append(ObserverPlant.ObserverPlantBuilder() \
                            .Price(int(x['price'])) \
                            .PlantVariety(x['variety']) \
                            .Email(x['email']) \
                            .Name(x['name']) \
                            .build())
        return observer
