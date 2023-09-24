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

