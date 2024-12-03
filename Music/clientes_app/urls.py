from django.urls import path
from clientes_app import views

urlpatterns = [
    path("cliente", views.inicio_vistaCliente, name="cliente"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    path("seleccionarCliente/<codigo>", views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente"),
    path("borrarCliente/<codigo>", views.borrarCliente, name="borrarCliente"),
]
