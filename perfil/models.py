from django.db import models
from django.contrib.auth.models import AbstractUser


class Cliente(AbstractUser):
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)

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

