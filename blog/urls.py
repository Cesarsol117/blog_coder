from django.urls import path
from blog.views import *
from usuarios.views import *

urlpatterns = [
    path("", inicio, name= "inicio"), 
    
]