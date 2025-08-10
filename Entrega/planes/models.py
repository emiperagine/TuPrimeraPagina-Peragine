from django.db import models

# Create your models here.

class Clases(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
  
class Plan(models.Model):
    nombre = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=8)
    clases_incluidas = models.ManyToManyField(Clases, related_name='plan')

    def __str__(self):
        return (f'Plan: {self.plan}')
    
    


# plan_oro = Planes('Oro', 60000)

# plan_plata = Planes('Plata', 48000)

# plan_bronce = Planes('Bronce', 38000)

