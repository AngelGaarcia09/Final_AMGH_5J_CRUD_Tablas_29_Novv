from django.db import models

# Create your models here.
class Trabajador(models.Model):
    id_trabajador=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    curp=models.CharField(max_length=100)
    telefono=models.PositiveIntegerField()
    fecha_nacimiento=models.DateField(null=False,blank=False)
    salario=models.DecimalField(max_digits=10, decimal_places=2)
    puesto=models.CharField(max_length=20)

    
    def __str__(self):
        return self.nombre