from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group


class Refeicoes(models.Model):
    alimento = models.CharField(max_length=100)
    quantidade = models.FloatField()
    horario = models.TimeField()
    
    def __str__(self):
        return self.alimento

class TabelaNutricional(models.Model):
    usuarioReferencia = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'paciente'})
    usuarioPeso = models.FloatField()
    gorduraCorporal = models.FloatField()
    refeicoes = models.ManyToManyField(Refeicoes)
    objetivo = models.CharField(max_length=200)
    exames = models.CharField(max_length=200, null=True)
    
    def clean(self):
        # Verifica se o usuário referenciado pertence ao grupo "paciente"
        if self.usuarioReferencia.groups.filter(name='paciente').exists():
            super().clean()
        else:
            raise ValidationError('O usuário deve pertencer ao grupo "paciente".')

    def __str__(self):
        return f"Tabela Nutricional de {self.usuarioReferencia.username}"


