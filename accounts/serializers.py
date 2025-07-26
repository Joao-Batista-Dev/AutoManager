from rest_framework import serializers
from accounts.models import Customer, Saller


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'cpf', 'telephone', 'address', 'created_at', 'update_at',]

        def validate_cpf(self, value):
            if len(value) != 11:
                raise serializers.ValidationError('CPF deve ter 11 dígitos.')
            return value
        
        def validate_telephone(self, value):
            if len(value) != 9:
                raise serializers.ValidationError('Seu Telefone dever conter 9 dígitos')
            return value


class SallerSerializers(serializers.ModelSerializer):
        class Meta:
            model = Saller
            fields = ['id', 'name', 'customer', 'telephone', 'created_at', 'update_at',]

        def validate_telephone(self, value):
            if len(value) != 9:
                raise serializers.ValidationError('Seu Telefone dever conter 9 dígitos')
            return value