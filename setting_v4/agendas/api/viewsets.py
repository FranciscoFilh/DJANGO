from rest_framework import viewsets
from agendas.models import Agenda
from .seliazers import AgendaSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer