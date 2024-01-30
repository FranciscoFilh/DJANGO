from django.urls import path, include
from rest_framework import routers
from .api.viewsets import CadastroViewSet

router = routers.DefaultRouter()
router.register(r'cadastro', CadastroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]