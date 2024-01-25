from django.db import models

class Cadastro(models.Model):
    name =  models.CharField(max_length=120, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    rg = models.CharField(max_length=14, blank=False, null=False)
    date_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=False)
    address = models.CharField(max_length=150)
    cep = models.CharField(max_length=10, blank=True, null=True)
    date_cad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name