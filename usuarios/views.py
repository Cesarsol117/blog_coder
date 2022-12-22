from django.shortcuts import render

from .models import *
from django.http import HttpResponse
from usuarios.forms import *
# clases
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# -------------
# para el formulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
# para restriciones
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def userPage(request):
    return render(request, "user.html")

# login creacion de usuarios
def login_request(request):
    if request.method == 'POST':
        form =  AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario1 = form.cleaned_data.get("username")
            clave1 = form.cleaned_data.get("password")

            usuario = authenticate(username = usuario1, password = clave1)
            # trae un usuario de la base, que tenga ese usuario y ese password....
            if usuario is not None:
                login(request, usuario)
                return render(request, 'inicio.html', {'mensaje':f"bienvenido {usuario}"})
            else:
                print("aqui es")
                return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", "form": form})
        else:
            print("aqui voy")
            return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", "form": form}) 
           

    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# register
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, 'inicio.html', {'mensaje':"usuario creado correctamente"})
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})