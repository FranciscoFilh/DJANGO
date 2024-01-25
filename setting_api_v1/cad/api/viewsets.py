from rest_framework import viewsets
from .serializers import CadastroSerializer
from cad.models import Cadastro

class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer