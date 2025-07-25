from django.contrib import admin
from accounts.models import Customer, Saller


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'cpf', 'telephone', 'address',]
    search_fields = ['id', 'name', 'cpf', 'email', 'telephone', 'address',]
    list_filter = ['id', 'name', 'cpf', 'email', 'telephone', 'address',]
    ordering = ['-id',]


@admin.register(Saller)
class SallerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'customer', 'telephone',]
    search_fields = ['id', 'name', 'customer__name',]
    list_filter = ['id', 'name', 'customer__name',]
    ordering = ['-id']