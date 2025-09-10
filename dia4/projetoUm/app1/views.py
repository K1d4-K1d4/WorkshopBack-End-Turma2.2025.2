from django.shortcuts import render
from .models import Endereco
from .forms import EnderecoForm
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView #Import para ClassBasedViews
from django.urls import reverse_lazy
import requests

# Create your views here.
class ViaCepFormView(FormView):
    template_name = 'viacep/viacep_form.html' #Template que será usado
    form_class = EnderecoForm
    success_url = reverse_lazy('viacep:lista')


    def form_valid(self,form): #Valida o formulário(assim no template é possível checar se deu certo, senão retorna um feedback de erro)
        cep = form.cleaned_data['cep']
        response = requests.get(f'http://viacep.com.br/ws/{cep}/json', verify=False)
        
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                endereco = Endereco(
                    cep=data.get('cep'),
                    rua=data.get('logradouro'),
                    bairro=data.get('bairro'),
                    cidade=data.get('localidade'),
                    estado=data.get('uf')
                    )
                endereco.save()
            else:
                form.add_error('cep', 'Erro ao consultar a API ViaCEP')
                return self.form_invalid(form)
            
        return super().form_valid(form) 
              #super() é usado para fazer essa alteração na classe 
               
class ViaCepListView(ListView):
    template_name= "viacep/viacep_list.html"
    model= Endereco
    context_object_name="enderecos"

class ViaCepDeleteView(DeleteView):
    template_name= "viacep/viacep_delete.html"
    model= Endereco
    context_object_name="enderecos"
    success_url = reverse_lazy('viacep:lista')


class ViaCepDetailView(DetailView):
    template_name= "viacep/viacep_detail.html"
    model= Endereco
    context_object_name="enderecos"


'''

def consulta_cep(request):
    form = EnderecoForm(request.GET or None)    
    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = requests.get(f'http://viacep.com.br/ws/{cep}/json')

        if response.status_code == 200:
            data = response.json()
            endereco = Endereco(
                cep=data.get('cep'),
                rua=data.get('logradouro'),
                bairro=data.get('bairro'),
                cidade=data.get('localidade'),
                estado=data.get('uf')
            )
            endereco.save()
    return render(request,'consulta_cep.html',{'endereco':endereco})
'''
'''    
class ViaCepList(ListView):

class ViaCepDetail(DetailView):

class ViaCepDelete(DeleteView):

class ViaCepUpdate(UpdateView):
'''

'''
def index(request):
    return render(request,'index.html')'''