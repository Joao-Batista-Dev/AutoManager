from rest_framework import serializers
from sales.models import SalesProposal, Vend


class VendSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vend
        fields = ['id', 'customer', 'saller', 'vehicle', 'date_sale', 'payment', 'value', 'update_at',]


class SalesProposalSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalesProposal
        fields = ['id', 'status', 'customer', 'vehicle', 'value', 'date_proposal', 'update_at',]