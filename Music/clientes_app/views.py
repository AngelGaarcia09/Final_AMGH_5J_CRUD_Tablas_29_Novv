from django.shortcuts import render, redirect
from .models import Cliente

def inicio_vistaCliente(request):
    los_clientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"mis_clientes": los_clientes})

def registrarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    dnl = request.POST["txtdnl"]
    id_compra = request.POST["numidcompra"]
    direccion = request.POST["txtdireccion"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]
    rfc = request.POST["txtrfc"]
    apellidos = request.POST["txtapellidos"]

    Cliente.objects.create(
        id_cliente=id_cliente, nombre=nombre, dnl=dnl, id_compra=id_compra,
        direccion=direccion, fecha_nacimiento=fecha_nacimiento,
        rfc=rfc, apellidos=apellidos
    )
    return redirect("cliente")

def seleccionarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    fecha_nacimiento = cliente.fecha_nacimiento.strftime('%Y-%m-%d')
    return render(request, "editarCliente.html", {"mi_cliente": cliente, "fecha_nacimiento": fecha_nacimiento})

def editarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    dnl = request.POST["txtdnl"]
    id_compra = request.POST["numidcompra"]
    direccion = request.POST["txtdireccion"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]
    rfc = request.POST["txtrfc"]
    apellidos = request.POST["txtapellidos"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.dnl = dnl
    cliente.id_compra = id_compra
    cliente.direccion = direccion
    cliente.fecha_nacimiento = fecha_nacimiento
    cliente.rfc = rfc
    cliente.apellidos = apellidos
    cliente.save()
    return redirect("cliente")

def borrarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    cliente.delete()
    return redirect("cliente")
