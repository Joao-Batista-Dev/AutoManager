from django.db import models
from accounts.models import Customer, Saller
from vehicles.models import Vehicle


class Vend(models.Model):
    PAYMENT_OPTION_STATUS = [
        ('PIX', 'Pix'),
        ('DEBITO', 'Debito'),
        ('CREDITO', 'Credito'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente',)
    saller = models.ForeignKey(Saller, on_delete=models.CASCADE, verbose_name='Vendedor',)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Veiculo',)
    date_sale = models.DateTimeField(auto_now_add=True, verbose_name='Data da Venda',)
    payment = models.CharField(choices=PAYMENT_OPTION_STATUS, default='CREDITO', verbose_name='Metodo Pagamento',)
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Final',)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em',)

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
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Final',)
    date_proposal = models.DateTimeField(auto_now_add=True, verbose_name='Data da Prosposta',)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em',)

    class Meta:
        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'