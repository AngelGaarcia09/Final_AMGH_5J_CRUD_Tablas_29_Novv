from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_codigoSucursal=models.PositiveIntegerField(primary_key=True)
    nombre_sucursal=models.CharField(max_length=100)
    ubicacion=models.CharField(max_length=100)
    horario=models.CharField(max_length=50)
    num_telefono=models.PositiveIntegerField()
    email=models.EmailField(max_length=50)
    estado=models.BooleanField()

    def __str__(self):
        return self.nombre_sucursal