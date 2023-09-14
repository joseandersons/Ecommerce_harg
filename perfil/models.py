from django.db import models
from django.contrib.auth.models import AbstractUser


class Cliente(AbstractUser):
    telefone = models.CharField(max_length=15, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    # complemento = models.CharField(max_length=30)
    # cidade = models.CharField(max_length=30)
    # estado = models.CharField(max_length=30)
    # add depois



    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')


    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name="cliente_groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name="cliente_user_permissions",
    )

    def __str__(self):
        return self.username

