from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, register, delete_carro
from rest_framework import routers
from .api.viewsets import AlugarCarroViewSet

router = routers.DefaultRouter()
router.register(r'alugar_carros', AlugarCarroViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('delete/<int:id>', delete_carro, name='delete'),
    path('api_alugar_carros', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)