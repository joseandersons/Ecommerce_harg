from django.db import models

# Create your models here.

class Grupo(models.Model):
    nome = models.CharField(max_length=255)
    pausado = models.CharField(default='N', max_length=1)

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True, blank=True)
    preco_original = models.FloatField(default=0)
    preco_promocional = models.FloatField(default=0)
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    pausado = models.CharField(default='N', max_length=1)

