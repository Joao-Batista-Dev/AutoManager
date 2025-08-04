from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from sales.models import Vend, SalesProposal
from sales.serializers import VendSerializers, SalesProposalSerializers


class VendApiV1ViewSet(ModelViewSet):
    queryset = Vend.objects.all()
    serializer_class = VendSerializers
    permission_classes = [IsAuthenticated,]


class SalesProposalApiV1ViewSet(ModelViewSet):
    queryset = SalesProposal.objects.all()
    serializer_class = SalesProposalSerializers
    permission_classes = [IsAuthenticated,]