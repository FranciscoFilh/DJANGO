from rest_framework import viewsets
from alugar_carros.models import AlugarCarro
from .serializer import AlugarCarroSerializer

class AlugarCarroViewSet(viewsets.ModelViewSet):
    queryset = AlugarCarro.objects.all()
    serializer_class = AlugarCarroSerializer