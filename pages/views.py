from django.http import JsonResponse
from django.shortcuts import render
from produto.models import Produto, Grupo


def dashboard(request):
    return render(request, 'dashboard.html')

def principal(request):
    return render(request, 'index.html')

