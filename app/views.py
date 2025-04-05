from rest_framework import generics, status
from rest_framework.response import Response
from .models import Estacionamiento
from .serializers import EstacionamientoSerializer


class EstacionamientoListCreateView(generics.ListCreateAPIView):
    serializer_class = EstacionamientoSerializer

    def get_queryset(self):
        # Solo vehículos que no tienen fecha de salida (activos)
        estacionamientos_activos = Estacionamiento.objects.filter(fecha_salida__isnull=True).order_by('-fecha')

        # Filtrar para devolver solo uno por patente (el más reciente)
        registros_filtrados = []
        patentes_agregadas = set()
        for est in estacionamientos_activos:
            if est.patente not in patentes_agregadas:
                registros_filtrados.append(est)
                patentes_agregadas.add(est.patente)

        return registros_filtrados

    def create(self, request, *args, **kwargs):
        # Evitar múltiples ingresos con la misma patente activa
        patente = request.data.get("patente")
        if Estacionamiento.objects.filter(patente=patente, fecha_salida__isnull=True).exists():
            return Response(
                {"error": "Ya existe un vehículo activo con esta patente."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)
