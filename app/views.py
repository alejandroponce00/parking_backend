from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Estacionamiento
from .serializers import EstacionamientoSerializer


class EstacionamientoListCreateView(generics.ListCreateAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer

@api_view(['POST'])
def marcar_pagado(request, pk):
    try:
        estacionamiento = Estacionamiento.objects.get(pk=pk)
        estacionamiento.marcar_como_pagado()
        serializer = EstacionamientoSerializer(estacionamiento)
        return Response(serializer.data)
    except Estacionamiento.DoesNotExist:
        return Response(
            {'error': 'Estacionamiento no encontrado'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_400_BAD_REQUEST
        )
   
