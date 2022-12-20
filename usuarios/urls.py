from django.contrib import admin
from django.urls import path
from usuarios.views import *
# se importa el logout directamente al url
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    # path('', inicio, name = "inicio"),
    path('login/', login_request, name = "login"),
    path('register/', register, name = "register"),
    # path('insumos/', insumos, name = "insumos"),
    # path('repuestos/', repuestos, name = "repuestos"),
    # path('tecnico/', tecnico, name = "tecnico"),
]