from rest_framework import serializers #
from .models import Endereco

#Class nomeDaModel(serializers.ModelSerializer)
class EnderecoSerializer(serializers.ModelSerializer):
   class Meta:
   #  Model = Modelo que será baseado
      model = Endereco
      fields = '__all__' #Preenche o serializer com todos os dados(usado no json())
      read_only_fields = ['logradouro','localidade','uf','bairro']
   #  ↑ Define que o usuário não pode enviar esses dados, apenas o CEP
