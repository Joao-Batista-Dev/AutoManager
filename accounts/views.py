from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from accounts.models import Customer, Saller
from accounts.serializers import CustomerSerializers, SallerSerializers


class CustomerApiV1ViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    permission_classes = [IsAuthenticated,]


class SallerApiV1ViewSet(ModelViewSet):
    queryset = Saller.objects.all()
    serializer_class = SallerSerializers
    permission_classes = [IsAuthenticated,]