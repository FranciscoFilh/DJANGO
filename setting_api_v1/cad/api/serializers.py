from rest_framework import serializers
from cad.models import Cadastro

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['nome', 'sobrenome', 'cpf', 'email', 'idade', 'data_nascimento', 'telefone']