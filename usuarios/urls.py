from django.contrib import admin
from django.urls import path
from usuarios.views import *
# se importa el logout directamente al url
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', userPage, name = "user"),
    path('login/', login_request, name = "login"),
    path('register/', register, name = "register"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    # path('repuestos/', repuestos, name = "repuestos"),
    # path('tecnico/', tecnico, name = "tecnico"), 
]