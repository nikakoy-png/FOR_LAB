from abc import ABC, abstractmethod

from MODELS.User import User


class UserDAO(ABC):
    @abstractmethod
    def addNewUser(self, user: User): pass

    @abstractmethod
    def delUserByID(self, ID: int): pass

    @abstractmethod
    def getUserByID(self, ID: int) -> User: pass

    @abstractmethod
    def getAllUsers(self) -> list or User: pass

    @abstractmethod
    def updateUser(self, user: User, ID: int): pass

    @abstractmethod
    def GetUserByUsernamePassword(self, username: str, password: str): pass
