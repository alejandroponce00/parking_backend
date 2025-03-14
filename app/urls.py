from django.urls import path
from .views import EstacionamientoListCreateView, marcar_pagado  # Importa las vistas

urlpatterns = [
    path('estacionamientos/', EstacionamientoListCreateView.as_view(), name='estacionamiento-list-create'),
    path('estacionamientos/<int:pk>/pagar/', marcar_pagado, name='marcar-pagado'),
]  # Define las URLs y las vistas asociadas