from rest_framework import serializers
from .models import Estacionamiento

class EstacionamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamiento
        fields = '__all__'  # Incluye todos los campos
