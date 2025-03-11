from rest_framework import serializers
from .models import Estacionamiento

class EstacionamientoSerializer(serializers.ModelSerializer):
    tiempo_estacionado = serializers.SerializerMethodField()
    tarifa_actual = serializers.SerializerMethodField()

    class Meta:
        model = Estacionamiento
        fields = ['id', 'vehiculo', 'patente', 'ubicacion', 'fecha', 'tarifa', 
                 'cupon_gratis', 'tarifa_por_hora', 'tiempo_estacionado', 'tarifa_actual']

    def get_tiempo_estacionado(self, obj):
        return obj.tiempo_transcurrido()

    def get_tarifa_actual(self, obj):
        return str(obj.calcular_tarifa())
