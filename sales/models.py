from django.db import models
from accounts.models import Customer, Saller
from vehicles.models import Vehicle


class Vend(models.Model):
    PAYMENT_OPTION_STATUS = [
        ('PIX', 'Pix'),
        ('DEBITO', 'Debito'),
        ('CREDITO', 'Credito'),
    ]

    VEND_STATUS_CHOICES = [
        ('AGUARDANDO', 'Aguardando'),
        ('ACEITA', 'Aceita'),
        ('RECUSADA', 'Recusada'),
    ]


    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente',)
    saller = models.ForeignKey(Saller, on_delete=models.CASCADE, verbose_name='Vendedor',)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Veiculo',)
    date_sale = models.DateTimeField(verbose_name='Data da Venda',)
    payment = models.CharField(choices=PAYMENT_OPTION_STATUS, default='CREDITO', verbose_name='Metodo Pagamento',)
    value = models.IntegerField(verbose_name='Valor Final',)



    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'


class SalesProposal(models.Model):
    STATUS_CHOICES = [
        ('AGUARDANDO', 'Aguardando'),
        ('ACEITA', 'Aceita'),
        ('RECUSADA', 'Recusada'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, default='AGUARDANDO', verbose_name='Status da Proposta',)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente',)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Veiculo',)
    value = models.IntegerField(verbose_name='Valor Final',)
    date_proposal = models.DateTimeField(verbose_name='Data da Prosposta',)
