from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='customers',
        verbose_name='Usuário',
    )
    name = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        max_length=100,
        blank='True',
        null='True',
        verbose_name='E-mail',
    )
    cpf = models.CharField(
        max_length=15,
        verbose_name='CPF'
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Telefone'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

