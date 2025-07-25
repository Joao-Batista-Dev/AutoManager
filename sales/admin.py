from django.contrib import admin
from sales.models import Vend, SalesProposal

@admin.register(Vend)
class VendAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'saller', 'vehicle', 'date_sale', 'payment', 'value', 'update_at',]
    search_fields = ['id', 'customer__name', 'saller', 'vehicle',]
    list_filter = ['id', 'customer__name', 'saller', 'vehicle',]
    ordering = ['-id',]


@admin.register(SalesProposal)
class SalesProposal(admin.ModelAdmin):
    list_display = ['id', 'status', 'customer', 'vehicle', 'date_proposal', 'value', 'update_at',]
    search_fields = ['id', 'status', 'customer__name', 'vehicle', 'date_proposal',]
    list_filter = ['id', 'status', 'customer__name', 'vehicle', 'date_proposal',]
    ordering = ['-id',]

