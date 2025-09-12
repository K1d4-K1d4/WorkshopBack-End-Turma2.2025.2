import requests #Biblioteca para requisições HTTP, usada para interagir com a API
from .models import Endereco
from .serializers import EnderecoSerializer
from rest_framework import viewsets

class EnderecoViewSet(viewsets.ModelViewSet): #Classe padrão da RestFramework que agrupa operações CRUD
   queryset = Endereco.objects.all()
   serializer_class = EnderecoSerializer
   
   def perform_create(self,serializer):
      cep = serializer.validated_data['cep']#Função para validar o CEP
      response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")#Conexão com a API(e requisitar os Dados Json)
      
      if response.status_code == 200:
         data = response.json() #Atribui a data os dados enviados pela API
         if 'erro' not in data:
            serializer.save(
               logradouro = data.get('logradouro'),
               bairro = data.get('bairro'),
               localidade = data.get('localidade'),
               uf = data.get('uf')
            )
         else:
            serializer.save()
      else:
         serializer.save()