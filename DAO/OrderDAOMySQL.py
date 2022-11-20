from DAO.OrderDAO import OrderDAO
import logging as lg
from datetime import datetime

from DB.MySQL import MySQL
from MODELS.Order import Order


class OrderDAOMySQL(OrderDAO):
    def __init__(self):
        self.mysql = MySQL()

    """Транзакція"""
    def makeOrder(self, ID_user: int, ID_plant: int):
        try:
            plant_q =(f"SELECT * FROM mydb_for_nsql.Plant where plant_id = {ID_plant}")
            result = self.mysql.execute_read_query(plant_q)
            print(result)
            if result == []:
                return None
            query = (
                    "INSERT INTO `mydb_for_nsql`.`order` (`date_of_make`)"
                    "VALUE ('%s')" % (str(datetime.today()).split()[0]))
            self.mysql.cursor.execute(query)
            self.mysql.cnx.commit()
            query = (f"SELECT LAST_INSERT_ID()")
            result = self.mysql.execute_read_query(query)
            query = ("INSERT INTO `mydb_for_nsql`.`user_order` (`Order_order_id`, `User_user_id`) VALUE ('%s', '%s')" %
                     (result[0][0], ID_user))
            self.mysql.cursor.execute(query)
            query = ("INSERT INTO `mydb_for_nsql`.`plant_order` (`plant_id`, `order_id`) VALUE ('%s', '%s')" %
                     (ID_plant, result[0][0]))
            self.mysql.cursor.execute(query)
            self.mysql.cnx.commit()
        except ValueError as e:
            lg.error(f'FATAL ERROR INCORRECT DATA {e}')

    def getOrderByID(self, ID: int) -> int:
        order = None
        try:
            query = (f"""SELECT mydb_for_nsql.order.order_id as order_id, mydb_for_nsql.order.date_of_make as date_of_make, plant_order.plant_id as plant_id, 
(SELECT User_user_id FROM mydb_for_nsql.user_order WHERE Order_order_id = mydb_for_nsql.order.order_id) as user_id
FROM mydb_for_nsql.order
INNER JOIN mydb_for_nsql.plant_order ON plant_order.order_id = mydb_for_nsql.order.order_id
LEFT JOIN mydb_for_nsql.user_order ON user_order.User_user_id = mydb_for_nsql.order.order_id where mydb_for_nsql.order.order_id = {ID};""")
            result = self.mysql.execute_read_query(query)
            order = Order.OrderBuilder()\
                .IdOrder(result[0][0])\
                .UserID(result[0][-1])\
                .PlantID(result[0][-2])\
                .Date(str(result[0][1]))\
                .build()
            return order
        except Exception as e:
            lg.error(f'{e}')

    def saveFunc(self):
        try:
            query = (f"""CALL e();""")
            result = self.mysql.execute_read_query(query)
            return result
        except Exception as e:
            lg.error(f'{e}')

