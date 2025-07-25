from rest_framework.viewsets import ModelViewSet
from accounts.models import Customer, Saller
from accounts.serializers import CustomerSerializers, SallerSerializers


class CustomerApiV1ViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class SallerApiV1ViewSet(ModelViewSet):
    queryset = Saller.objects.all()
    serializer_class = SallerSerializers