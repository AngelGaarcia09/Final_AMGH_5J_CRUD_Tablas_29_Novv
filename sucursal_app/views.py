from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.
def inicio_vistaSucursal(request):
    lassucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursal.html", {"missucursales": lassucursales})

def registrarSucursal(request):
    id_codigoSucursal = request.POST["txtcodigo"]
    nombre_sucursal = request.POST["txtnombre"]
    ubicacion = request.POST["txtubicacion"]
    horario = request.POST["txthorario"]
    num_telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    estado = request.POST.get("chkestado") == "on"

    Sucursal.objects.create(
        id_codigoSucursal=id_codigoSucursal,
        nombre_sucursal=nombre_sucursal,
        ubicacion=ubicacion,
        horario=horario,
        num_telefono=num_telefono,
        email=email,
        estado=estado,
    )  # GUARDA EL REGISTRO

    return redirect("sucursal")

def seleccionarSucursal(request,codigo):
    sucursal = Sucursal.objects.get(id_codigoSucursal=codigo)
    return render(request, "editarSucursal.html", {"missucursales": sucursal})

def editarSucursal(request):
    id_codigoSucursal = request.POST["txtcodigo"]
    nombre_sucursal = request.POST["txtnombre"]
    ubicacion = request.POST["txtubicacion"]
    horario = request.POST["txthorario"]
    num_telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    estado = request.POST.get("chkestado") == "on"

    sucursal = Sucursal.objects.get(id_codigoSucursal=id_codigoSucursal)
    sucursal.nombre_sucursal = nombre_sucursal
    sucursal.ubicacion = ubicacion
    sucursal.horario = horario
    sucursal.num_telefono = num_telefono
    sucursal.email = email
    sucursal.estado = estado
    sucursal.save()  # GUARDA EL REGISTRO ACTUALIZADO

    return redirect("sucursal")

def borrarSucursal(request, codigo):
    sucursal = Sucursal.objects.get(id_codigoSucursal=codigo)
    sucursal.delete()  # BORRA EL REGISTRO
    return redirect("sucursal")
