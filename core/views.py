from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PessoaForm
from .models import Pessoa
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

# Views do Formulario

#Caso tenha sido enviado o post cria uma pessoa com dados do form
def create(request):
    form = PessoaForm(request.POST)
    #Caso nao valido, para por aqui
    if not form.is_valid():
        context = {'form':form}
        return render(request, 'core/pessoashome.html',context)

    #Caso valido, continua
    Pessoa.objects.create(**form.cleaned_data)
    return HttpResponseRedirect('/pessoashome/')

#Caso nao tenha sido enviado post, abre form em branco
def new(request):
    context={'form':PessoaForm()}
    return render(request, 'core/pessoashome.html', context)

def pessoashome(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)