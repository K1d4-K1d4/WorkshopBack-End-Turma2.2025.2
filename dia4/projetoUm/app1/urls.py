from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consulta_cep/', views.consulta_cep, name='consulta_cep')
]
