from django.urls import path, include
from rest_framework import routers
from vehicles.views import VehicleApiv1ViewSet, TestDriveApiv1ViewSet

router = routers.SimpleRouter()
router.register('vehicle', VehicleApiv1ViewSet, basename='vehicle')
router.register('testdrive', TestDriveApiv1ViewSet, basename='testdrive')

urlpatterns = [
    path('', include(router.urls)),
]
