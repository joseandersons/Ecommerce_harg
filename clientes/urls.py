from django.urls import include, path
from . import views


app_name = 'clientes'


urlpatterns = [
    path('', views.principal, name='principal'), 
    path('consulta-restaurantes/', views.consulta_restaurantes, name='consulta_restaurantes'),
    path('consulta-produtos-loja/<int:loja_id>/', views.consulta_produtos_loja, name='consulta_produtos_loja'),
    path('login-cliente/', views.login_cliente, name='login_cliente'),
    path('cadastro-cliente/', views.criar_conta_cliente, name='criar_conta_cliente'),
    path('logout-cliente', views.logout_cliente, name='logout_cliente'),

    path('adicionar-item-carrinho/', include('pedido.urls', namespace='pedido')),
    
] 