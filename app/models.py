from django.db import models
from django.utils import timezone  # Importar timezone

class Estacionamiento(models.Model):
    vehiculo = models.CharField(max_length=50)
    patente = models.CharField(max_length=10, unique=True)
    ubicacion = models.TextField()
    fecha = models.DateTimeField(verbose_name="Fecha de ingreso", default=timezone.now)  # Agregar default

    def __str__(self):
        return f"{self.vehiculo} - {self.patente}"

