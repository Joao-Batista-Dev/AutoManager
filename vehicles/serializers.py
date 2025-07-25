from rest_framework import serializers
from vehicles.models import Vehicle, TestDrive


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'brand', 'year', 'color', 'mileage', 'price', 'description', 'available', 'created_at', 'update_at',]


class TestDriveSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = ['id', 'customer', 'vehicle', 'scheduling', 'confirmed', 'update_at',]