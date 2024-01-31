from django.db import models

class Consulta(models.Model):
    TURNO_CHOICES = (
        ('MA', 'Manha'),
        ('TA', 'Tarde'),
        ('NO', 'Noite'),
    )

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=14)
    turno = models.CharField(max_length=3, choices=TURNO_CHOICES)
    dia_consulta = models.DateField()
    horario_consulta = models.TimeField()

    def __str__(self):
        return self.nome