from django.db import models

class Reuniao(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao =  models.CharField(max_length=200, blank=False, null=False)
    local = models.CharField(max_length=100, blank=False, null=False)
    nome_participante = models.CharField(max_length=100, blank=False, null=False)
    dia = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return self.titulo