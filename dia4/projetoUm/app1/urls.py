from django.urls import path
from . import views

app_name = "viacep"

urlpatterns = [
    path('', views.ViaCepFormView.as_view(), name='index'),
    path('lista/', views.ViaCepListView.as_view(), name='lista'),
    path('detalhe/<int:pk>/', views.ViaCepDetailView.as_view(), name='detail'),
    path('excluir/<int:pk>/', views.ViaCepDeleteView.as_view(), name='delete'),
]
