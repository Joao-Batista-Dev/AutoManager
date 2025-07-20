from django.contrib import admin
from models import Customer, Saller


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cpf', 'telephone', 'address',]
    