from django.db import models
from django.utils import timezone
from decimal import Decimal
from math import ceil

class Estacionamiento(models.Model):
    vehiculo = models.CharField(max_length=50)
    patente = models.CharField(max_length=10, unique=True)
    ubicacion = models.TextField()
    fecha = models.DateTimeField(verbose_name="Fecha de ingreso", default=timezone.now)
    fecha_salida = models.DateTimeField(null=True, blank=True)  # 👈 NUEVO CAMPO
    tarifa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Precio en dólares")
    cupon_gratis = models.BooleanField(default=False)
    tarifa_por_hora = models.DecimalField(max_digits=5, decimal_places=2, default=2.00, help_text="Tarifa base por hora en dólares")

    def __str__(self):
        return f"{self.vehiculo} - {self.patente}"
    
    def calcular_tarifa(self):
        if self.cupon_gratis:
            return Decimal('0.00')
        
        tiempo_final = self.fecha_salida or timezone.now()
        tiempo_transcurrido = tiempo_final - self.fecha
        
        horas = ceil(tiempo_transcurrido.total_seconds() / 3600)
        return self.tarifa_por_hora * Decimal(str(horas))
    
    def tiempo_transcurrido(self):
        tiempo_final = self.fecha_salida or timezone.now()
        tiempo = tiempo_final - self.fecha
        horas = tiempo.total_seconds() // 3600
        minutos = (tiempo.total_seconds() % 3600) // 60
        
        return f"{int(horas)}h {int(minutos)}m"
