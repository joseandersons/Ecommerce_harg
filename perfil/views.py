from django.shortcuts import render

def login_cliente(request):
    return render(request, 'login.html')


def criar_conta_cliente(request):
    return render(request, 'criar-conta-cliente.html')