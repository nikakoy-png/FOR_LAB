from DAO.PlantDAO import PlantDAO
from DAO.UserDAO import UserDAO
from MODELS.Plant import Plant
from MODELS.User import User


def check_access(role: list, user: User):
    for r in role:
        if r == user.getPermission:
            return True
    return False


class PlantProxy(PlantDAO):
    def __init__(self, plantDAO: PlantDAO) -> None:
        self._dao_plant = plantDAO

    def getAllPlantsByUser(self, ID_user: int, user: User = None) -> list:
        if check_access(['user', 'admin'], user):
            return self._dao_plant.getAllPlantsByUser(1)
        else:
            raise PermissionError

    def getPlantByID(self, ID: int, user: User = None) -> Plant:
        if check_access(['user', 'admin'], user):
            return self._dao_plant.getPlantByID(ID)
        else:
            raise PermissionError

    def getPlantByMAXPrice(self, user: User = None) -> list or Plant:
        if check_access(['user', 'admin'], user):
            return self._dao_plant.getPlantByMAXPrice()
        else:
            raise PermissionError

    def getPlantByMINPrice(self, user: User = None) -> list or Plant:
        if check_access(['user', 'admin'], user):
            return self._dao_plant.getPlantByMINPrice()
        else:
            raise PermissionError

    def delPlant(self, ID: int, user: User = None):
        if check_access(['admin'], user):
            self._dao_plant.delPlant(ID)
            return
        else:
            raise PermissionError

    def updatePlant(self, plant: Plant, ID: int, user: User = None):
        if check_access(['admin'], user):
            self._dao_plant.updatePlant(plant, ID)
            return
        else:
            raise PermissionError

    def addNewPlant(self, plant: Plant, user: User = None):
        if check_access(['admin'], user):
            self._dao_plant.addNewPlant(plant)
            return
        else:
            raise PermissionError
