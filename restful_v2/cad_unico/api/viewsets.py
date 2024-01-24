from rest_framework import viewsets
from .serializers import BeneficiariosSerialixer
from cad_unico.models import Beneficiarios

class BeneficiarisViewSet(viewsets.ModelViewSet):
    queryset = Beneficiarios.objects.all()
    serializer_class = BeneficiariosSerialixer