from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.adicionar_carrinho_js, name='adicionar_carrinho_js'),
    path('consultar-carrinho/', views.consultar_carrinho, name='consultar_carrinho'),
    path('finalizar-pedido/', views.adicionar_carrinho_banco, name='adicionar_carrinho_banco'),

]
