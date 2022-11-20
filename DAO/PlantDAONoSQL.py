from datetime import datetime

from bson import ObjectId

from DAO.PlantDAO import PlantDAO
from DB.NoSQL import NoSQL
from MODELS.Plant import Plant


class PlantDAONoSQL(PlantDAO):
    def __init__(self):
        self.nosql = NoSQL().collection_plant

    def getAllPlantsByUser(self, ID_user: int) -> list:
        plant = []
        for x in self.nosql.find({}):
            plant.append(Plant.PlantBuilder() \
                         .Prolific(x['prolific']) \
                         .Growth(x['growth']) \
                         .Description(x['description']) \
                         .Sun_loving(x['sun_loving']) \
                         .Variety(x['variety']) \
                         .Price(x['price']) \
                         .build())
        return plant

    def getPlantByID(self, ID) -> Plant:
        x = self.nosql.find_one({'_id': ObjectId(ID)})
        plant = Plant.PlantBuilder() \
            .Prolific(x['prolific']) \
            .Growth(x['growth']) \
            .Description(x['description']) \
            .Sun_loving(x['sun_loving']) \
            .Variety(x['variety']) \
            .Price(x['price']) \
            .build()
        return plant

    def getPlantByMAXPrice(self) -> list or Plant:
        plant = []
        for x in self.nosql.find().sort("price", -1).allow_disk_use(True):
            plant.append(Plant.PlantBuilder() \
                         .Prolific(x['prolific']) \
                         .Growth(x['growth']) \
                         .Description(x['description']) \
                         .Sun_loving(x['sun_loving']) \
                         .Variety(x['variety']) \
                         .Price(x['price']) \
                         .build())
        return plant

    def getPlantByMINPrice(self) -> list or Plant:
        plant = []
        for x in self.nosql.find().sort("price", 1):
            plant.append(Plant.PlantBuilder() \
                         .Prolific(x['prolific']) \
                         .Growth(x['growth']) \
                         .Description(x['description']) \
                         .Sun_loving(x['sun_loving']) \
                         .Variety(x['variety']) \
                         .Price(x['price']) \
                         .build())
        return plant

    def delPlant(self, ID: int):
        self.nosql.delete_one({'_id': ObjectId(ID)})

    def updatePlant(self, plant: Plant, ID: int):
        self.nosql.update_one({'_id': ObjectId(ID)}, {'$set': {"variety": plant.getVariety,
                                                                          "price": plant.getPrice,
                                                                          "growth": plant.getGrowth,
                                                                          "sun_loving": plant.getSun_loving,
                                                                          "description": plant.getDescription,
                                                                          "prolific": plant.getProlific}})

    def addNewPlant(self, plant: Plant):
        request = {
            'variety': plant.getVariety,
            'price': int(plant.getPrice),
            'growth': int(plant.getGrowth),
            'sun_loving': plant.getSun_loving,
            'description': plant.getDescription,
            'prolific': plant.getProlific,
            'date_of_creation': str(datetime.today()).split()[0]
        }
        self.nosql.insert_one(request)
