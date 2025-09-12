from rest_framework import serializers
from .models import Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'#Pega todos as informações da requisição
        read_only_fields = ['rua', 'bairro', 'cidade', 'estado']#Mas só serão exibidos essas
