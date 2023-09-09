from django.db import models

# Create your models here.

class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    pausado = models.CharField(default='N', max_length=1)

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True, blank=True)
    preco_original = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    preco_promocional = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    pausado = models.CharField(default='N', max_length=1)

def __str__(self):
        return self.name

