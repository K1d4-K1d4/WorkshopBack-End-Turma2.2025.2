from rest_framework import viewsets
from .models import Endereco
from .serializers import EnderecoSerializer
import requests

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    
    def perform_create(self, serializer):
        cep = serializer.validated_data['cep']
        response = requests.get(f'http://viacep.com.br/ws/{cep}/json/', verify= False)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'erro' not in data:
                # Preenche os dados do endereço com os dados da API
                serializer.save(
                    rua=data.get('logradouro', ''),
                    bairro=data.get('bairro', ''),
                    cidade=data.get('localidade', ''),
                    estado=data.get('uf', ''),
                    cep=data.get('cep', cep)  # Usa o CEP formatado da API se disponível
                )
            else:
                # Se a API retornar erro, salva apenas com o CEP
                serializer.save()
        else:
            # Em caso de erro na API, salva apenas com o CEP
            serializer.save()
        # consumir a api do via cep e armazenar no serializer