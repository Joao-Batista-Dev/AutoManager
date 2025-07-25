from rest_framework.viewsets import ModelViewSet
from vehicles.models import Vehicle, TestDrive
from vehicles.serializers import VehicleSerializers, TestDriveSerializers


class VehicleApiv1ViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializers


class TestDriveApiv1ViewSet(ModelViewSet):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializers