from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    dnl=models.CharField(max_length=100)
    id_compra=models.PositiveIntegerField()
    direccion=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField(null=False,blank=False)
    rfc=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=100)

    
    def __str__(self):
        return self.nombre