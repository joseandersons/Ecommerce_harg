from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.adicionar_carrinho, name='adicionar_carrinho'),

]
