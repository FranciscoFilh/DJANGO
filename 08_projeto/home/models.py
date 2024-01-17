from django.db import models

class Livro(models.Model):
    nome_do_livro = models.CharField(max_length=100)
    ano_da_publicacao = models.IntegerField(max_length=4)
    quantidade_de_paginas = models.IntegerField(max_length=3)
    nome_do_autor = models.CharField(max_length=20)
    nome_da_editora = models.CharField(max_length=20)
    preco = models.FloatField(default=0.0)

    def __str__(self):
        return self.nome_do_livro