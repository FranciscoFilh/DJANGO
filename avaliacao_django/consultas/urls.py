from django.urls import path, include
from .views import index, cadastro, deletar
from rest_framework import routers
from .api.viewsets import ConsultaViewSet

router = routers.DefaultRouter()
router.register('api_consultas', ConsultaViewSet)

urlpatterns = [
    path('',index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('api_consultas/', include(router.urls)),
]