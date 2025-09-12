from django.contrib import admin #Django básico
from django.urls import path, include #Django básico + include para manuseio de url
from rest_framework.routers import DefaultRouter #Ferramenta para criar um conjunto completo de URLs para o viewset do app
from consulta.viewsets import EnderecoViewSet #Busca a viewset do app para relacionar com o DefaultRouter

router = DefaultRouter()
router.register(r'enderecos', EnderecoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
