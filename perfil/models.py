from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    is_loja = models.BooleanField(default=False)
    cidade = models.CharField(max_length=30)
   
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name="us_groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name="us_user_permissions",
    )

    def __str__(self):
        return self.username



class Cliente(Usuario):

    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)


    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

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
    

   