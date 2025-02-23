from django.db import models

# Create your models here.
class Estacionamiento(models.Model):
    vehiculo = models.CharField(max_length=50)
    patente= models.CharField(max_length=100)
    ubicacion= models.TextField()

    def __str__(self):
        return self.patente