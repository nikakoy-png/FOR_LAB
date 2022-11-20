from DAO.PlantDAO import PlantDAO
import logging as lg
from datetime import datetime

from DB.MySQL import MySQL
from MODELS.Plant import Plant


class PlantDAOMySQL(PlantDAO):
    def __init__(self):
        self.mysql = MySQL()

    def addNewPlant(self, plant: Plant):
        try:
            query = (
                    "INSERT INTO `mydb_for_nsql`.`plant` (`variety`, `price`, `growth`, `sun_loving`, `description`, `prolific`,"
                    "`date_of_creation`)"
                    "VALUE ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (plant.getVariety, plant.getPrice,
                                                                          plant.getGrowth, plant.getSun_loving,
                                                                          plant.getDescription, plant.getProlific,
                                                                          str(datetime.today()).split()[0]))
            self.mysql.cursor.execute(query)
            self.mysql.cnx.commit()
        except ValueError as e:
            lg.error(f'FATAL ERROR INCORRECT DATA {e}')

    def getPlantByID(self, ID: int) -> Plant:
        plant = None
        try:
            query = (f"SELECT * FROM mydb_for_nsql.Plant where plant_id = {ID}")
            result = self.mysql.execute_read_query(query)
            print(result)
            plant = Plant.PlantBuilder() \
                .Prolific(result[0][6]) \
                .Growth(result[0][3]) \
                .Description(result[0][5]) \
                .Sun_loving(result[0][4]) \
                .Variety(result[0][1]) \
                .Price(result[0][2]) \
                .build()
        except Exception as e:
            lg.error(f'{e}')

        return plant

    def getPlantByMINPrice(self) -> list or Plant:
        plant = []
        try:
            query = (f"SELECT * FROM mydb_for_nsql.Plant ORDER BY price")
            result = self.mysql.execute_read_query(query)
            for x in result:
                plant.append(Plant.PlantBuilder() \
                             .Prolific(x[6]) \
                             .Growth(x[3]) \
                             .Description(x[5]) \
                             .Sun_loving(x[4]) \
                             .Variety(x[1]) \
                             .Price(x[2]) \
                             .build())
        except Exception as e:
            lg.error(f'{e}')

        return plant

    def getPlantByMAXPrice(self) -> list or Plant:
        plant = []
        try:
            query = (f"SELECT * FROM mydb_for_nsql.Plant ORDER BY price DESC")
            result = self.mysql.execute_read_query(query)
            for x in result:
                plant.append(Plant.PlantBuilder() \
                             .Prolific(x[6]) \
                             .Growth(x[3]) \
                             .Description(x[5]) \
                             .Sun_loving(x[4]) \
                             .Variety(x[1]) \
                             .Price(x[2]) \
                             .build())
        except Exception as e:
            lg.error(f'{e}')

        return plant

    def getAllPlantsByUser(self, ID_user: int) -> list:
        plant = []
        try:
            query = (f"SELECT * FROM mydb_for_nsql.Plant")
            result = self.mysql.execute_read_query(query)
            for x in result:
                plant.append(Plant.PlantBuilder() \
                             .Prolific(x[6]) \
                             .Growth(x[3]) \
                             .Description(x[5]) \
                             .Sun_loving(x[4]) \
                             .Variety(x[1]) \
                             .Price(x[2]) \
                             .build())
        except Exception as e:
            lg.error(f'{e}')

        return plant

    def updatePlant(self, plant: Plant, ID):
        try:
            query = (f"UPDATE mydb_for_nsql.plant SET variety='%s', price='%s', "
                     f"growth='%s', sun_loving='%s', description='%s',"
                     f"prolific='%s'"
                     f" WHERE plant_id = {ID}" % (
                     plant.getVariety, plant.getPrice, plant.getGrowth, plant.getSun_loving,
                     plant.getDescription, plant.getProlific))
            self.mysql.cursor.execute(query)
            self.mysql.cnx.commit()
        except Exception as e:
            lg.error(f'{e}')

    def delPlant(self, ID: int):
        try:
            query = (f"DELETE FROM mydb_for_nsql.plant WHERE plant_id = '%s'" % (ID))
            self.mysql.cursor.execute(query)
            self.mysql.cnx.commit()
        except Exception as e:
            lg.error(f'{e}')
