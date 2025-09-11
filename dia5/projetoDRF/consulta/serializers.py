from rest_framework import serializers
from .models import Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
        read_only_fields = ['rua', 'bairro', 'cidade', 'estado']
