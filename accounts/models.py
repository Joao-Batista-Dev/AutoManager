from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='Cliente',)
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF',)
    telephone = models.CharField(max_length=9,verbose_name='Telefone',)
    address = models.CharField(max_length=255, verbose_name='Endereço',)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now, verbose_name='Criando em',)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em',)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.user
    

class Saller(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome',)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null= True, verbose_name='Cliente',)
    telephone = models.CharField(max_length=9, verbose_name='Telefone',)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now, verbose_name='Criando em',)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em',)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.name
