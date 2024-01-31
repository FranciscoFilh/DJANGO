from django.db import models

class Agenda(models.Model):
    DIAS_CHOICES = (
        ('SEG', 'Segunda'),
        ('TER', 'Terça'),
        ('QUA', 'Quarta'),
        ('QUI', 'Quinta'),
        ('SEX', 'Sexta'),
        ('SAB', 'Sábado'),
    )

    diciplina = models.CharField(max_length=100)
    assunto = models.TextField()
    tempo_estudado = models.IntegerField()
    dias = models.CharField(max_length=3, choices=DIAS_CHOICES)
    foto = models.ImageField(upload_to='assunto')

    def __str__(self):
        return self.diciplina