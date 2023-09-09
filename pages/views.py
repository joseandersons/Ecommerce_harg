from django.shortcuts import render
from produto.models import Produto, Grupo


def dashboard(request):
    return render(request, 'dashboard.html')

def consulta_grupo(request):
    return render(request, 'consulta-grupos.html')

def consulta_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'consulta-produtos.html', {'produtos': produtos})

# def cadastrar_produto(request):
#     grupos = Grupo.objects.all()
#     context = {'grupos': grupos}
#     return render(request, 'cadastro-produto.html', context) 

