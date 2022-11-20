from DAO.UserDAONoSQL import UserDAONoSQL
from Factory.CreatorDAO import CreatorDAO
from DAO.UserDAO import UserDAO
from DAO.UserDAOMySQL import UserDAOMySQL


class UserDAOCreator(CreatorDAO):
    def factory_method(self, type_db: str) -> UserDAOMySQL | UserDAONoSQL:
        if type_db == "MYSQL":
            return UserDAOMySQL()
        elif type_db == "MONGODB":
            return UserDAONoSQL()
