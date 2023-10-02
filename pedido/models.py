from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

from lojas.models import Loja



class Pedido(models.Model):
    usuario = models.ForeignKey('clientes.Cliente', null=True, blank=True, on_delete=models.CASCADE)
    total = models.FloatField(default=0.0)
    data_hora = models.DateTimeField(auto_now_add=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, default=None)
    forma_pgt = models.CharField(max_length=255, default="null")
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('p', 'Producão'),
            ('d', 'Despachado'),
            ('F', 'Finalizado'),
        )
    )
    def __str__(self):
        return f'Pedido N. {self.pk}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.CharField(max_length=255)
    preco = models.FloatField()
    quantidade = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='prodto_carrinho/%Y/%m', blank=True, null=True)
    subtotal = models.FloatField()


    def __str__(self):
        return f'Item do N. {self.pk}'
    
class Meta:
    verbose_name = 'Item do pedido'
    verbose_name_plural = 'Itens do pedido'
