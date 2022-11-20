from DAO.OrderDAO import OrderDAO
from MODELS.User import User


def check_access(role: list, user: User):
    for r in role:
        if r == user.getPermission:
            return True
    return False


class OrderProxy(OrderDAO):
    def __init__(self, orderDAO: OrderDAO) -> None:
        self._dao_order = orderDAO

    def makeOrder(self, ID_user: int, ID_plant: int, user: User = None):
        if check_access(['user', 'admin'], user):
            self._dao_order.makeOrder(ID_user, ID_plant)
        else:
            raise PermissionError

    def getOrderByID(self, ID: int,  user: User = None):
        if check_access(['user', 'admin'], user):
            return self._dao_order.getOrderByID(ID)
        else:
            raise PermissionError

    def saveFunc(self,  user: User = None):
        if check_access(['user', 'admin'], user):
            return self._dao_order.saveFunc()
        else:
            raise PermissionError
