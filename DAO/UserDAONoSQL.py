from bson import ObjectId

from DAO.UserDAO import UserDAO
from DB.NoSQL import NoSQL
from MODELS.User import User


class UserDAONoSQL(UserDAO):
    def __init__(self):
        self.nosql = NoSQL().collection_user

    def addNewUser(self, user: User):
        if NoSQL().collection_user.find_one({'username': user.getUsername}) is not None:
            return None
        request = {
            'email': user.getEmail,
            'username': user.getUsername,
            'password': user.getPassword,
            'phone_number': user.getPhoneNumber,
            'permission': 'user',
        }
        self.nosql.insert_one(request)

    def delUserByID(self, ID: int):
        self.nosql.delete_one({'_id': ObjectId(ID)})

    def getUserByID(self, ID: int) -> User:
        x = self.nosql.find_one({'_id': ObjectId(ID)})
        user = User.UserBuilder() \
            .Username(x['username']) \
            .Password(x['password']) \
            .Email(x['email']) \
            .Phone_number(x['phone_number']) \
            .Permission(x['permission']) \
            .build()
        return user

    def getAllUsers(self) -> list or User:
        user = []
        for x in self.nosql.find({}):
            user.append(User.UserBuilder() \
                        .Username(x['username']) \
                        .Password(x['password']) \
                        .Email(x['email']) \
                        .Phone_number(x['phone_number']) \
                        .Permission(x['permission']) \
                        .build())
        return user

    def updateUser(self, user: User, ID: int):
        self.nosql.update_one({'_id': ObjectId(ID)}, {'$set': {"username": user.getUsername,
                                                               "password": user.getPassword,
                                                               "email": user.getEmail,
                                                               "phone_number": user.getPhoneNumber,
                                                               "permission": user.getPermission}})

    def GetUserByUsernamePassword(self, username: str, password:str):
        x = self.nosql.find_one({'username': username, 'password': password})
        user = User.UserBuilder() \
            .Username(x['username']) \
            .Password(x['password']) \
            .Email(x['email']) \
            .Phone_number(x['phone_number']) \
            .Permission(x['permission']) \
            .build()
        return user

