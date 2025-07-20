from django.db import models
from accounts.models import Customer

class Vehicle(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome',)
    brand = models.CharField(max_length=255, blank=True, null=True, verbose_name='Marca',)
    year = models.IntegerField(max_length=4, blank=True, null=True, verbose_name='Ano',)
    color = models.CharField(max_length=255, blank=True, null=True, verbose_name='Cor',)
    mileage = models.IntegerField(max_length=10, blank=True, null=True, verbose_name='Quilometragem',)
    price = models.IntegerField(max_length=10, blank=True, null=True, verbose_name='Valor Veiculo',)
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descrição',)
    available = models.BooleanField(default=False, verbose_name='Disponivel',), 
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Criando em',)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em',)

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.name


class TestDrive(models.Model):
    custome = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Veiculo')
    scheduling = models.DateTimeField(verbose_name='Data')
    confirmed = models.BooleanField(default=False, verbose_name='Confirmado')
    
    class Meta:
        verbose_name = 'Teste Drive'
        verbose_name_plural = 'Teste Drives'