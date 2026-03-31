from django.urls import path
from .views import listar_jogadores, jogadores_ativos

urlpatterns = [
    path('jogadores/', listar_jogadores),
    path('jogadores/ativos/', jogadores_ativos),
]