from django.contrib import admin
from vehicles.models import Vehicle, TestDrive


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'year', 'color', 'mileage', 'price', 'description', 'available', 'created_at', 'update_at',]
    search_fields =  ['id', 'name', 'brand', 'year',  'created_at',]
    list_filter =  ['id', 'name', 'brand', 'year',  'created_at',]
    ordering = ['-id',]


@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'vehicle', 'scheduling', 'confirmed', 'update_at',]
    search_fields = ['id', 'customer__name', 'vehicle', 'scheduling', 'confirmed', 'update_at',]
    list_filter = ['id', 'customer__name', 'vehicle', 'scheduling', 'confirmed', 'update_at',]
    ordering = ['-id',]