from DAO.OrderDAOMySQL import OrderDAOMySQL
from DAO.OrderDAONoSQL import OrderDAONoSQL
from Factory.CreatorDAO import CreatorDAO


class OrderDAOCreator(CreatorDAO):
    def factory_method(self, type_db: str) -> OrderDAOMySQL | OrderDAONoSQL:
        if type_db == "MYSQL":
            return OrderDAOMySQL()
        elif type_db == "MONGODB":
            return OrderDAONoSQL()
