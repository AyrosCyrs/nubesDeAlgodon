from django.shortcuts import render, redirect
from django.conf import settings
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import environ
env = environ.Env()
environ.Env.read_env()

def inicio(request):
    ctx = {
        "site_name": env("SITE_NAME"),
        "site_version": env("SITE_VERSION"),
    }
    return render(request, "inventario/inicio.html", ctx)

def productos(request):
    ctx = {
        "site_name": env("SITE_NAME"),
        "site_version": env("SITE_VERSION"),
    }
    return render(request, "inventario/productos.html", ctx)

def acerca_de(request):
    ctx = {
        "site_name": env("SITE_NAME"),
        "site_version": env("SITE_VERSION"),
    }
    return render(request, "inventario/acerca.html", ctx)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"]
            )
            login(request, user)
            return redirect(to="inventario:inicio")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)