from DAO.UserDAO import UserDAO
from MODELS.User import User


def check_access(role: list, user: User):
    for r in role:
        if r == user.getPermission:
            return True
    return False


class UserProxy(UserDAO):
    def __init__(self, userDAO: UserDAO) -> None:
        self._dao_user = userDAO

    def addNewUser(self, user: User, user_: User = None):
        self._dao_user.addNewUser(user)

    def delUserByID(self, ID: int, user_: User = None):
        if check_access(['admin'], user_):
            self._dao_user.delUserByID(ID)
        else:
            raise PermissionError

    def getUserByID(self, ID: int, user_: User = None) -> User:
        if check_access(['admin'], user_):
            return self.getUserByID(ID)
        else:
            raise PermissionError

    def getAllUsers(self, user_: User = None) -> list or User:
        if check_access(['admin'], user_):
            return self._dao_user.getAllUsers()
        else:
            raise PermissionError

    def updateUser(self, user: User, ID: int, user_: User = None):
        if check_access(['admin'], user_):
            self._dao_user.updateUser(user, ID)
        else:
            raise PermissionError

    def GetUserByUsernamePassword(self, username: str, password: str):
        return self._dao_user.GetUserByUsernamePassword(username, password)
