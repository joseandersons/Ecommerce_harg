from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('consultar-carrinho/', views.consultar_carrinho, name='consultar_carrinho'),

]
