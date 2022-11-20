import logging as lg
from DAO.UserDAO import UserDAO
from DB.MySQL import MySQL
from MODELS.User import User


class UserDAOMySQL(UserDAO):
    def __init__(self):
        self.mysql = MySQL()

    def addNewUser(self, user: User):
        try:
            check = ("SELECT * FROM mydb_for_nsql.user where username = '%s'" % (user.getUsername))
            result = self.mysql.execute_read_query(check)
            if len(result) is not 0:
                return None
            query = ("INSERT INTO `mydb_for_nsql`.`user` (`username`, `password`, `email`, `phone_number`, `permission_id`)"
                     "VALUE ('%s', '%s', '%s', '%s', '%s')" % (
                         user.getUsername, user.getPassword, user.getEmail, user.getPhoneNumber, 1))
            self.mysql.cursor.execute(query)
            self.mysql.cnx.commit()
        except ValueError as e:
            lg.error(f'FATAL ERROR INCORRECT DATA {e}')

    def getUserByID(self, ID: int) -> User:
        user = None
        try:
            query = (f"SELECT * FROM mydb_for_nsql.user where user_id = {ID}")
            result = self.mysql.execute_read_query(query)
            user = User.UserBuilder() \
                .Username(result[0][2]) \
                .Password(result[0][3]) \
                .Email(result[0][1]) \
                .Phone_number(result[0][4]) \
                .Permission(result[0][5]) \
                .build()
        except Exception as e:
            lg.error(f'{e}')

        return user

    def getAllUsers(self) -> list or User:
        user = []
        try:
            query = (f"SELECT * FROM mydb_for_nsql.user")
            result = self.mysql.execute_read_query(query)
            for x in result:
                user.append(User.UserBuilder() \
                            .Username(x[2]) \
                            .Password(x[3]) \
                            .Email(x[1]) \
                            .Phone_number(x[4]) \
                            .Permission(x[5]) \
                            .build())
        except Exception as e:
            lg.error(f'{e}')

        return user

    def updateUser(self, user: User, ID: int):
        try:
            query = (f"UPDATE mydb_for_nsql.user SET `username`='%s', `password`='%s', "
                     f"`email`='%s', `phone_number`='%s' WHERE `user_id` = '%s'" % (
                         user.getUsername, user.getPassword, user.getEmail, user.getPhoneNumber, ID))
            self.mysql.cursor.execute(query)
            self.mysql.cnx.commit()
        except Exception as e:
            lg.error(f'{e}')

    def delUserByID(self, ID: int):
        try:
            query = (f"DELETE FROM mydb_for_nsql.user WHERE `user_id` = {ID}")
            self.mysql.cursor.execute(query)
            self.mysql.cnx.commit()
        except Exception as e:
            lg.error(f'{e}')

    def GetUserByUsernamePassword(self, username: str, password: str):
        try:
            query = (f"SELECT * FROM mydb_for_nsql.user where `username` = '%s' AND `password` = '%s'") % (username,
                                                                                                        password)
            result = self.mysql.execute_read_query(query)
            print(result)
            user = User.UserBuilder() \
                .Username(result[0][2]) \
                .Password(result[0][3]) \
                .Email(result[0][1]) \
                .Phone_number(result[0][4]) \
                .Permission(result[0][5]) \
                .build()
            print(user)
            return user
        except Exception as e:
            lg.error(f'{e}')