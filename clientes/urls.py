from django.urls import include, path
from . import views


app_name = 'clientes'


urlpatterns = [
    path('', views.principal, name='principal'), 
    path('login-cliente/', views.login_cliente, name='login_cliente'),
    path('cadastro-cliente/', views.criar_conta_cliente, name='criar_conta_cliente'),
] 