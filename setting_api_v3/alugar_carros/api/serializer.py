from rest_framework import serializers
from alugar_carros.models import AlugarCarro

class AlugarCarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlugarCarro
        fields = '__all__'