from django.db import models
from accounts.models import Customer


class Vehicle(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome',)
    brand = models.CharField(max_length=255, blank=True, null=True, verbose_name='Marca',)
    year = models.IntegerField(blank=True, null=True, verbose_name='Ano',)
    color = models.CharField(max_length=255, blank=True, null=True, verbose_name='Cor',)
    mileage = models.IntegerField(blank=True, null=True, verbose_name='Quilometragem',)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor Veiculo',)
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descrição',)
    available = models.BooleanField(default=False, verbose_name='Disponivel',)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criando em',)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em',)

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.name


class TestDrive(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Veiculo')
    scheduling = models.DateTimeField(verbose_name='Data do Teste Drive')
    confirmed = models.BooleanField(default=False, verbose_name='Confirmado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em',)
    
    class Meta:
        verbose_name = 'Teste Drive'
        verbose_name_plural = 'Teste Drives'