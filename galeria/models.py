from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, primary_key=True)
    
    def __str__(self):
        return self.nome

class Administrador(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Refeicoes(models.Model):
    alimento = models.CharField(max_length=100)
    quantidade = models.FloatField()
    horario = models.DateTimeField()
    
    def __str__(self):
        return self.alimento

class TabelaNutricional(models.Model):
    usuarioReferencia = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    usuarioPeso = models.FloatField()
    gorduraCorporal = models.FloatField()
    refeicoes = models.ManyToManyField(Refeicoes)
    objetivo = models.CharField(max_length=200)
    exames = models.TextField()
    
    def __str__(self):
        return f"Tabela Nutricional de {self.usuarioReferencia.nome}"
