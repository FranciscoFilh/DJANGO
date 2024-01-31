from rest_framework import viewsets
from reunioes.models import Reuniao
from .selializers import ReuniaoSerializer

class ReuniaoViewSet(viewsets.ModelViewSet):
    queryset = Reuniao.objects.all()
    serializer_class = ReuniaoSerializer