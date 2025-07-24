from django.contrib import admin
from sales.models import Vend, SalesProposal

@admin.register(Vend)
class VendAdmin(admin.ModelAdmin):
    list_display = ['customer', 'saller', 'vehicle', 'date_sale', 'payment', 'value', 'update_at',]
    search_fields = ['customer', 'saller', 'vehicle',]
    list_filter = ['customer', 'saller', 'vehicle',]
    ordering = ['-id',]


@admin.register(SalesProposal)
class SalesProposal(admin.ModelAdmin):
    list_display = ['status', 'customer', 'vehicle', 'date_proposal', 'value', 'update_at',]
    search_fields = ['status', 'customer', 'vehicle', 'date_proposal',]
    list_filter = ['status', 'customer', 'vehicle', 'date_proposal',]
    ordering = ['-id',]

