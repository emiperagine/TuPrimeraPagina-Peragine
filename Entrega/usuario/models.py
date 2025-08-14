from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.DecimalField(max_digits=2, decimal_places=2)

def __str__(self):
    return (f'Nombre: {self.nombre} | Edad: {self.edad}')

