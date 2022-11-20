from DAO.PlantDAONoSQL import PlantDAONoSQL
from Factory.CreatorDAO import CreatorDAO
from DAO.PlantDAOMySQL import PlantDAOMySQL


class PlantDAOCreator(CreatorDAO):
    def factory_method(self, type_db: str) -> PlantDAOMySQL | PlantDAONoSQL:
        if type_db == "MYSQL":
            return PlantDAOMySQL()
        elif type_db == "MONGODB":
            return PlantDAONoSQL()
