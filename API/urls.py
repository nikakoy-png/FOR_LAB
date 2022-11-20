from django.urls import re_path, path, include
from API import views

urlpatterns = [
    re_path(r'register/', views.RegisterUser),
    path(r'delUser/<slug:ID_user>', views.DelUserByID),
    path(r'getUser/<slug:ID_user>', views.GetUserByID),
    re_path(r'getAllUser/', views.GetAllUsers),
    path(r'updateUser/<slug:ID_user>', views.UpdateUser),

    path(r'getPlantByID/<slug:ID_plant>', views.GetPlantByID),
    re_path(r'getPlantByMAXPrice/', views.GetPlantByMAXPrice),
    re_path(r'getPlantByMINPrice/$', views.GetPlantByMINPrice),
    path(r'delPlant/<slug:ID_plant>', views.DelPlant),
    path(r'updatePlant/<slug:ID_plant>', views.UpdatePlant),
    re_path(r'addNewPlant/', views.AddPlant),

    path(r'makeOrder/<slug:ID_user>/plant/<slug:ID_plant>', views.MakeOrder),
    path(r'getOrderByID/<slug:ID_order>', views.GetOrderByID),


    re_path(r'saveFunc/', views.SaveFunc),
    re_path(r'productivityCheck/', views.ProductivityCheck),


    re_path(r'addObserver/', views.AddObserver),
    re_path(r'addObserver/', views.DelObserver),


    path(r'undoPlant/<slug:ID_plant>', views.UndoPlant),


    re_path(r'auth/', views.authenticate_user),
]
