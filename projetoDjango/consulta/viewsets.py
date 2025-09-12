from rest_framework import viewsets #Importa as classes viewsets no arquivo
from .models import Endereco #Importa o modelo criado na models.py
from .serializers import EnderecoSerializer #Importa o modelo de formulário
import requests #Requests é a biblioteca instalada para receber as informações da conexão com a API

#Viewsets são classes presentes no DjangoRest responsaveis por agrupar várias operações CRUD, assim com o uso de viewsets aumenta a complexidade do código mas se torna mais compacto e organizado.

class EnderecoViewSet(viewsets.ModelViewSet):
   #Variável que será usada para todas as operações CRUD
   queryset = Endereco.objects.all() #Atribui a variável queryset todos os objetos do modelo Endereco
   #Variável que será usada para definir qual form/serializer será usado nas operações
   serializer_class = EnderecoSerializer
   
   def perform_create(self,serializer):
      cep = serializer.validated_data['cep'] #Pega o cep já validado pelo serializer e atribui a variável CEP
      response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")#Aqui é criada a conexão com a API e é aonde atribuimos à variável o formulário da API
   
      if response.status_code == 200:
         data = response.json()#Atribuimos à data os valores retirados do formulário
         if "erro" not in data:#Se não existir "erro"
         #o serializer irá adicionar salvar em si os dados pegos na requisição
            serializer.save(
               cep=data.get('cep'),
               rua=data.get('logradouro'),
               bairro=data.get('bairro'),
               cidade=data.get('localidade'),
               estado=data.get('uf')
            )
         else:
            serializer.save()
      else:
         serializer.save()
      