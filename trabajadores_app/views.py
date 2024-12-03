from django.shortcuts import render, redirect
from .models import Trabajador

def inicio_vistaTrabajador(request):
    los_trabajadores = Trabajador.objects.all()
    return render(request, "gestionarTrabajador.html", {"mis_trabajadores": los_trabajadores})

def registrarTrabajador(request):
    id_trabajador = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    curp = request.POST["txtcurp"]
    telefono = request.POST["numtelefono"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]
    salario = request.POST["numsalario"]
    puesto = request.POST["txtpuesto"]
    
    Trabajador.objects.create(
        id_trabajador=id_trabajador, nombre=nombre, curp=curp, telefono=telefono,
        fecha_nacimiento=fecha_nacimiento, salario=salario, puesto=puesto
    )
    return redirect("trabajador")

def seleccionarTrabajador(request, codigo):
    trabajador = Trabajador.objects.get(id_trabajador=codigo)
    fecha_nacimiento = trabajador.fecha_nacimiento.strftime('%Y-%m-%d')
    return render(request, "editarTrabajador.html", {"mi_trabajador": trabajador, "mi_trabajador": trabajador, "fecha_nacimiento": fecha_nacimiento})

def editarTrabajador(request):
    id_trabajador = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    curp = request.POST["txtcurp"]
    telefono = request.POST["numtelefono"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]
    salario = request.POST["numsalario"]
    puesto = request.POST["txtpuesto"]

    trabajador = Trabajador.objects.get(id_trabajador=id_trabajador)
    trabajador.nombre = nombre
    trabajador.curp = curp
    trabajador.telefono = telefono
    trabajador.fecha_nacimiento = fecha_nacimiento
    trabajador.salario = salario
    trabajador.puesto = puesto
    trabajador.save()
    return redirect("trabajador")

def borrarTrabajador(request, codigo):
    trabajador = Trabajador.objects.get(id_trabajador=codigo)
    trabajador.delete()
    return redirect("trabajador")
