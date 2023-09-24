from functools import wraps
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def cliente_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_loja:
            logout(request)  # Desloga o usuário
            return redirect('clientes:principal')  # Redireciona para a página de login do cliente
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def user_is_loja(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_loja:
                return function(request, *args, **kwargs)
            else:
                # Se estiver autenticado mas não for loja, desloga o usuário
                logout(request)
        # Se não estiver autenticado ou não for loja, redirecione para o login de lojas
        return redirect('lojas:login_loja') 
    return wrap

