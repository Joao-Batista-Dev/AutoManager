from rest_framework import serializers
from accounts.models import Customer, Saller


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'cpf', 'telephone', 'address', 'created_at', 'update_at',]


class SallerSerializers(serializers.ModelSerializer):
        class Meta:
             model = Saller
             fields = ['id', 'name', 'customer', 'telephone', 'created_at', 'update_at',]