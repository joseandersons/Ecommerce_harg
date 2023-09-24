from django.db import models
from django.contrib.auth.models import User
# from lojas.models import Loja



class Pedido(models.Model):
    usuario = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)

    total = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)
    # loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
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
    imagem = models.CharField(max_length=2000)
    subtotal = models.FloatField()


    def __str__(self):
        return f'Item do N. {self.pk}'
    
class Meta:
    verbose_name = 'Item do pedido'
    verbose_name_plural = 'Itens do pedido'
