from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=70)
    sobrenome = models.CharField(max_length=70)
    cpf =  models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.nome