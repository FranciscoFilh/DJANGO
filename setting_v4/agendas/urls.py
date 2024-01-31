from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, cadastro, deletar
from rest_framework import routers
from .api.viewsets import AgendaViewSet

router = routers.DefaultRouter()
router.register('api_agendas', AgendaViewSet)

urlpatterns = [
    path('',index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('api_agendas/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
