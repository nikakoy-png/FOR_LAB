from DAO.ObserverDAONoSQL import ObserverDAONoSQL
from DAO.OrderDAOMySQL import OrderDAOMySQL
from DAO.OrderDAONoSQL import OrderDAONoSQL
from Factory.CreatorDAO import CreatorDAO


class ObserverDAOCreator(CreatorDAO):
    def factory_method(self, type_db: str) -> str | ObserverDAONoSQL:
        if type_db == "MYSQL":
            "mysql observer"
        elif type_db == "MONGODB":
            return ObserverDAONoSQL()
