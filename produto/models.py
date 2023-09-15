from django.db import models
from lojas.models import Loja


# Create your models here.

class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    pausado = models.CharField(default='N', max_length=1)

    def __str__(self):
            return self.nome

class Produto(models.Model):
    
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True, blank=True)
    preco_original = models.CharField(max_length=10, default='0')
    preco_promocional = models.CharField(max_length=10, default='0')
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    pausado = models.CharField(default='N', max_length=1)
    loja = models.ForeignKey(Loja, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
            return self.nome
    

