from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from consulta.viewsets import EnderecoViewSet

router = DefaultRouter()
router.register(r'enderecos', EnderecoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
