from django.urls import include, path
from . import views

urlpatterns = [
    
    path('login-cliente/', views.login_cliente, name='login_cliente'),
    path('login-loja/', views.login_loja, name='login_loja'),
    path('cadastro-cliente/', views.criar_conta_cliente, name='criar_conta_cliente'),
    path('cadastro-loja/', views.criar_conta_loja, name='criar_conta_loja'),
    
] 