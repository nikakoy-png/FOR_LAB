import datetime
import json
import random
import random

from django.http import HttpResponse
from django.shortcuts import render
import jwt
from jwt import InvalidSignatureError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Factory.CreateDAOSetting import CreateDAO
from Factory.OrderDAOCreator import OrderDAOCreator
from Factory.PlantDAOCreator import PlantDAOCreator
from Factory.UserDAOCreator import UserDAOCreator
from MODELS.Plant import Plant
from MODELS.User import User
from Memento.Memory import Memory
from Observer.ObserverPlant import ObserverPlant
from Observer.PlantSubject import PlantSubject
from Proxy.OrderProxy import OrderProxy
from Proxy.PlantProxy import PlantProxy
from Proxy.UserProxy import UserProxy
from django_back import settings

"""MEMENTO MEMORY"""
memory = Memory()

db_plant = PlantProxy(CreateDAO(PlantDAOCreator(), "MONGODB"))
db_user = UserProxy(CreateDAO(UserDAOCreator(), "MONGODB"))
db_order = OrderProxy(CreateDAO(OrderDAOCreator(), "MONGODB"))

subject = PlantSubject()

"""Сериализатор, для работы с моделями в формате JSON"""


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def GetAuthUser(token):
    data = jwt.decode(str(token), settings.SECRET_KEY, algorithms="HS256")['data']
    print(data)
    user = User.UserBuilder() \
        .Username(data['username']) \
        .Password(data['password']) \
        .Email(data['email']) \
        .Phone_number(data['phone_number']) \
        .Permission(data['permission']) \
        .build()
    return user


@api_view(['POST'])
def RegisterUser(request):
    if request.method == 'POST':
        request_j = json.loads(request.body)
        user = User.UserBuilder() \
            .Username(request_j['username']) \
            .Password(request_j['password1']) \
            .Email(request_j['email']) \
            .Phone_number(request_j['phone']) \
            .build()
        db_user.addNewUser(user)
    else:
        return HttpResponse({'Content-Type not supported!'})
    return HttpResponse({'GREAT!'})


@api_view(['POST'])
def DelUserByID(request, ID_user: int):
    if request.method == 'POST':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            db_user.delUserByID(ID_user, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return HttpResponse({'GREAT!'})


@api_view(['GET'])
def GetUserByID(request, ID_user: int):
    if request.method == 'GET':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            user = db_user.getUserByID(ID_user, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return Response({'result': json.dumps(user, cls=CustomEncoder)})


@api_view(['GET'])
def GetAllUsers(request):
    if request.method == 'GET':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            users = db_user.getAllUsers(request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return Response({'result': json.dumps(users, cls=CustomEncoder)})


@api_view(['POST'])
def UpdateUser(request, ID_user: int):
    if request.method == 'POST':
        request_j = json.loads(request.body)
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        user = User.UserBuilder() \
            .Username(request_j['username']) \
            .Password(request_j['password1']) \
            .Email(request_j['email']) \
            .Phone_number(request_j['phone']) \
            .build()
        try:
            db_user.updateUser(user, ID_user, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})

    else:
        return HttpResponse({'Content-Type not supported!'})
    return HttpResponse({'GREAT!'})


@api_view(['POST'])
def AddPlant(request):
    if request.method == 'POST':
        request_j = json.loads(request.body)
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        plant = Plant.PlantBuilder() \
            .Prolific(request_j['prolific']) \
            .Growth(request_j['growth']) \
            .Description(request_j['description']) \
            .Sun_loving(request_j['sun_loving']) \
            .Variety(request_j['variety']) \
            .Price(request_j['price']) \
            .build()
        try:
            db_plant.addNewPlant(plant, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
        subject.observer_business_logic(plant)
    else:
        return HttpResponse({'Content-Type not supported!'})
    return HttpResponse({'GREAT!'})


@api_view(['POST'])
def UpdatePlant(request, ID_plant: int):
    if request.method == 'POST':
        memory.backup(db_plant.getPlantByID(ID_plant), ID_plant)
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        request_j = json.loads(request.body)
        plant = Plant.PlantBuilder() \
            .Prolific(request_j['prolific']) \
            .Growth(request_j['growth']) \
            .Description(request_j['description']) \
            .Sun_loving(request_j['sun_loving']) \
            .Variety(request_j['variety']) \
            .Price(request_j['price']) \
            .build()
        try:
            db_plant.updatePlant(plant, ID_plant, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return HttpResponse({'GREAT!'})


@api_view(['POST'])
def DelPlant(request, ID_plant: int):
    if request.method == 'POST':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            db_plant.delPlant(ID_plant, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return HttpResponse({'GREAT!'})


@api_view(['GET'])
def GetPlantByMINPrice(request):
    if request.method == 'GET':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            plants = db_plant.getPlantByMINPrice(request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return Response({'result': json.dumps(plants, cls=CustomEncoder)})


@api_view(['GET'])
def GetPlantByMAXPrice(request):
    if request.method == 'GET':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            plants = db_plant.getPlantByMAXPrice(request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return Response({'result': json.dumps(plants, cls=CustomEncoder)})


@api_view(['GET'])
def GetAllPlantsByUser(request):
    if request.method == 'GET':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            plants = db_plant.getAllPlantsByUser(1, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return Response({'result': json.dumps(plants, cls=CustomEncoder)})


@api_view(['GET'])
def GetPlantByID(request, ID_plant: int):
    if request.method == 'GET':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            plant = db_plant.getPlantByID(ID_plant, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return Response({'result': json.dumps(plant, cls=CustomEncoder)})


@api_view(['POST'])
def MakeOrder(request, ID_user: int, ID_plant: int):
    if request.method == 'POST':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            db_order.makeOrder(ID_user, ID_plant, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return HttpResponse({'GREAT!'})


@api_view(['GET'])
def GetOrderByID(request, ID_order: int):
    if request.method == 'GET':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            order = db_order.getOrderByID(ID_order, request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return Response({'result': json.dumps(order, cls=CustomEncoder)})


@api_view(['GET'])
def SaveFunc(request):
    if request.method == 'GET':
        try:
            request_user = GetAuthUser(request.headers['Authorization'])
        except InvalidSignatureError:
            return HttpResponse({'TOKEN VERIFICATION FAILED'})
        try:
            orders = db_order.saveFunc(request_user)
        except PermissionError:
            return HttpResponse({'Permission ERROR! You can`t do it!'})
    else:
        return HttpResponse({'Content-Type not supported!'})
    return Response({'result': json.dumps(orders, cls=CustomEncoder)})


@api_view(['GET'])
def ProductivityCheck(request):
    if request.method == 'GET':
        print("Проверка продуктивности работы.")
        list_count_object = [100, 1000, 10000, 50000, 100000, 500000]
        for count in list_count_object:
            print(f"Проверка продуктивности работы на {count} обьектах.")
            print(f'Добавление {count} обьектов')
            start_time = datetime.datetime.now()
            for x in range(count):
                plant = Plant.PlantBuilder() \
                    .Prolific(random.choice([True, False])) \
                    .Growth(random.randint(3, 9)) \
                    .Description('description') \
                    .Sun_loving(random.choice([True, False])) \
                    .Variety('Kaktus') \
                    .Price(random.randint(150, 4500)) \
                    .build()
                db_plant.addNewPlant(plant)
            print(f'Время выполнения записи {count}: ', datetime.datetime.now() - start_time)
            print(f'Чтение {count} обьектов')
            start_time = datetime.datetime.now()
            db_plant.getPlantByMAXPrice()
            print(f'Время выполнения чтения {count}: ', datetime.datetime.now() - start_time)
    return HttpResponse({'GREAT!'})


@api_view(['POST'])
def AddObserver(request):
    if request.method == 'POST':
        request_j = json.loads(request.body)
        observer = ObserverPlant.ObserverPlantBuilder() \
            .Price(int(request_j['price'])) \
            .PlantVariety(request_j['variety']) \
            .Email(request_j['email']) \
            .Name(request_j['name']) \
            .build()
        subject.attach(observer)
    return HttpResponse({'GREAT!'})


@api_view(['POST'])
def UndoPlant(request, ID_plant: int):
    if request.method == 'POST':
        try:
            db_plant.updatePlant(memory.undo(ID_plant), ID_plant)
        except AttributeError:
            print('Object never used')
        memory.history()
    return HttpResponse({'GREAT!'})


@api_view(['POST'])
def authenticate_user(request):
    if request.method == 'POST':
        print(request.body)
        print(type(request.body))
        request_j = json.loads(request.body)
        username = request_j['username']
        password = request_j['password']
        try:
            user = db_user.GetUserByUsernamePassword(username, password)
        except TypeError:
            return HttpResponse({'USER IS NOT FOUND!!'})
        print(username)
        print(password)
        print(user)
        payload = {
                'username': user.getUsername,
                'password': user.getPassword,
                'email': user.getEmail,
                'phone_number': user.getPhoneNumber,
                'permission': user.getPermission
            }

        if user:
            token = jwt.encode({'data': payload}, settings.SECRET_KEY, algorithm='HS256')
            user_details = {}
            user_details['token'] = token
            print(user_details)
            return Response(user_details, status=status.HTTP_200_OK)
    return HttpResponse({'ERROR!'})


@api_view(['POST'])
def DelObserver(request, ID):
    if request.method == 'POST':
        subject.detach(ID)
    return HttpResponse({'GREAT!'})
