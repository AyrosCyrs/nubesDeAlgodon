from django.urls import path
from . import views

app_name = "inventario"

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('productos/', views.productos, name="productos"),
    path('acerca/', views.acerca_de, name="acerca"),
    path('registro/', views.registro, name="registro"),
]