import mysql.connector
from mysqlx import expr
import logging as lg

from SINGLETON.SingletonMeta import SingletonMeta


class MySQL(metaclass=SingletonMeta):
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', database='mydb_for_nsql', host='127.0.0.1', password='123123')
            self.cursor = self.cnx.cursor(buffered=True)
        except expr as e:
            lg.error("FATAL ERROR WITH CONNECTOR")

    def execute_read_query(self, query):
        cursor = self.cnx.cursor()
        result = None
        cursor.execute(query)
        result = cursor.fetchall()
        return result
