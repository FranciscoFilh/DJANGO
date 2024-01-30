from rest_framework import viewsets
from cat_filmes.models import Filme
from .selializer import FilmeSerializer

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer