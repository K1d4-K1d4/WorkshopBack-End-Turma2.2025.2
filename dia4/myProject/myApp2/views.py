from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home.html')
def resposta(request):
    variavel = {
        'resposta':'http://127.0.0.1:8000/myApp2/rebeca'
    }
    return render(request,'resposta.html',variavel)
