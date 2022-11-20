import logging as lg

from djoser.conf import User


class User(object):
    def __init__(self, userbuilder):
        self.__username = userbuilder._username
        self.__password = userbuilder._password
        self.__email = userbuilder._email
        self.__phone_number = userbuilder._phone_number
        self.__permission = userbuilder._permission

    @property
    def getUsername(self):
        return self.__username

    @property
    def getPermission(self):
        return self.__permission

    @property
    def getPassword(self):
        return self.__password

    @property
    def getEmail(self):
        return self.__email

    @property
    def getPhoneNumber(self):
        return self.__phone_number

    def setUsername(self, username):
        try:
            if type(username) != str:
                raise TypeError
            self.__username = username
        except TypeError:
            lg.error('Type Error')

    def setPassword(self, password):
        try:
            if type(password) != str:
                raise TypeError
            self.__username = password
        except TypeError:
            lg.error('Type Error')

    def setEmail(self, email):
        try:
            if type(email) != str:
                raise TypeError
            self.__username = email
        except TypeError:
            lg.error('Type Error')

    def setPhoneNumber(self, phone_number):
        try:
            if type(phone_number) != str:
                raise TypeError
            self.__username = phone_number
        except TypeError:
            lg.error('Type Error')

    def __str__(self):
        return f'*********************************\n' \
               f'username:{self.__username}\n' \
               f'phone_number:{self.__phone_number}\n' \
               f'password:{self.__password}\n' \
               f'email:{self.__email}\n' \
               f'*********************************'

    class UserBuilder:
        def __init__(self):
            self._username = str
            self._password = str
            self._email = str
            self._phone_number = str
            self._permission = int

        def Username(self, Variety: str):
            self._username = Variety
            return self

        def Password(self, Price: float | int):
            self._password = Price
            return self

        def Email(self, Growth: float | int):
            self._email = Growth
            return self

        def Phone_number(self, Sun_Loving: bool):
            self._phone_number = Sun_Loving
            return self

        def Permission(self, permission: int):
            self._permission = permission
            return self

        def build(self):
            return User(self)


