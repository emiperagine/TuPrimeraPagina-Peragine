from django.db import models

# Create your models here.


class Plan(models.Model):
    nombre = models.CharField(max_length=10)
    días = models.CharField(max_length=50)
    musculos_a_trabajar = models.CharField(max_length=200)
    foto_inicial = models.ImageField(upload_to="fotos_inicial", null=True)
    
    def __str__(self):
        return (f'Plan: {self.nombre}')