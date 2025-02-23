from django.urls import path
from .views import EstacionamientoListCreateView  # Importa la vista

urlpatterns = [
    path('estacionamientos/', EstacionamientoListCreateView.as_view(), name='estacionamiento-list-create'),
]  # Define la URL y la vista asociada