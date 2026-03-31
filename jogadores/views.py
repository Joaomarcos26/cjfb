from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Jogador

def listar_jogadores(request):
    jogadores = list(Jogador.objects.values())
    return JsonResponse(jogadores, safe=False)

def jogadores_ativos(request):
    jogadores = list(Jogador.objects.filter(status='ATIVO').values())
    return JsonResponse(jogadores, safe=False)