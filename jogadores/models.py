from django.db import models

# Create your models here.
from django.db import models

class Jogador(models.Model):

    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
    ]

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    naturalidade = models.CharField(max_length=100)
    origem = models.CharField(max_length=100)  # universidade/clube
    numero = models.IntegerField()
    time = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome