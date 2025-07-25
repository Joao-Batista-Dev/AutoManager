from rest_framework.viewsets import ModelViewSet
from sales.models import Vend, SalesProposal
from sales.serializers import VendSerializers, SalesProposalSerializers


class VendApiV1ViewSet(ModelViewSet):
    queryset = Vend.objects.all()
    serializer_class = VendSerializers


class SalesProposalApiV1ViewSet(ModelViewSet):
    queryset = SalesProposal
    serializer_class = SalesProposalSerializers