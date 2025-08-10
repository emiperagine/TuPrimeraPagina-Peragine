from django.db import models

# Create your models here.
class Planes(models.Model):
    plan = models.CharField(max_length=10)
    precio = models.CharField(max_length=10)

    def __str__(self):
        return (f'Plan: {self.plan}')
    
class Beneficio(models.Model):
    clases_incluidas = models.Charfield(max_length=20)
  

    def __str__(self):
        return (f'Clases incluidas en el plan {self.plan}: {self.clases_incluidas}.')
    
    

