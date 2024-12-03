from django.urls import path
from trabajadores_app import views

urlpatterns = [
    path("trabajador", views.inicio_vistaTrabajador, name="trabajador"),
    path("registrarTrabajador/", views.registrarTrabajador, name="registrarTrabajador"),
    path("seleccionarTrabajador/<codigo>", views.seleccionarTrabajador, name="seleccionarTrabajador"),
    path("editarTrabajador/", views.editarTrabajador, name="editarTrabajador"),
    path("borrarTrabajador/<codigo>", views.borrarTrabajador, name="borrarTrabajador"),
]
