from django.urls import path, include
from rest_framework import routers
from .api.viewsets import BeneficiarisViewSet

router = routers.DefaultRouter()
router.register(r'beneficiarios', BeneficiarisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
