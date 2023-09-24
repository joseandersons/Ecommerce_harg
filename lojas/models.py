from django.db import models

from core.models import Usuario


class Loja(Usuario):

    cnpj = models.CharField(max_length=18, null=True, blank=True) 
    pausado = models.CharField(default='N', max_length=1)
    horario_abertura = models.TimeField(null=True, blank=True)
    horario_fechamento = models.TimeField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    imagem = models.ImageField(upload_to='loja_imagens/%Y/%m', blank=True, null=True)

    
    TIPO_CULINARIA_CHOICES = [
        ('BR', 'Brasileira'),
        ('IT', 'Italiana'),
        ('AM', 'Americana'),
        ('JP', 'Japonesa'),
        ('OU', 'Outra'),
    ]
    tipo_culinaria = models.CharField(max_length=2, choices=TIPO_CULINARIA_CHOICES, default='OU')
    

