
from django.db import models
from django.utils import timezone

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateField(default=timezone.now)  # Defina o valor padrão aqui
    concluida = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo

