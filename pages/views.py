from django.http import JsonResponse
from django.shortcuts import render
from produto.models import Produto, Grupo


def dashboard(request):
    return render(request, 'dashboard.html')

def principal(request):
    if request.method == 'GET':
        nome_usuario = request.user.username if request.user.is_authenticated else 'Visitante'
        return render(request, 'index.html', {'nome_usuario': nome_usuario})
    else:
        return render(request, 'index.html')

