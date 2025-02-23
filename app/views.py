from rest_framework import generics
from .models import Estacionamiento
from .serializers import EstacionamientoSerializer


class EstacionamientoListCreateView(generics.ListCreateAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer
   
