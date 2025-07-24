from django.contrib import admin
from vehicles.models import Vehicle, TestDrive


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'year', 'color', 'mileage', 'price', 'description', 'available', 'created_at', 'update_at',]
    search_fields =  ['name', 'brand', 'year',  'created_at',]
    list_filter =  ['name', 'brand', 'year',  'created_at',]
    ordering = ['-id',]


@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    list_display = ['custome', 'vehicle', 'scheduling', 'confirmed', 'update_at',]
    search_fields = ['custome', 'vehicle', 'scheduling', 'confirmed', 'update_at',]
    list_filter = ['custome', 'vehicle', 'scheduling', 'confirmed', 'update_at',]
    ordering = ['-id',]