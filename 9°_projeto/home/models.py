from django.db import models

class Carne(models.Model):
    nome_da_carne = models.CharField(max_length=100)
    tipos_da_carne = models.CharField(max_length=100)
    data_do_corte = models.IntegerField()
    fazenda_que_vendeu_a_carne = models.CharField(max_length=100)
    preco = models.FloatField(default=0.0)

    def __str__(self):
        return self.nome_da_carne