from django.urls import path, include
from rest_framework import routers
from sales.views import VendApiV1ViewSet, SalesProposalApiV1ViewSet

router = routers.SimpleRouter()
router.register('vend', VendApiV1ViewSet, basename='vend')
router.register('selesproposal', SalesProposalApiV1ViewSet, basename='selesproposal')

urlpatterns = [
    path('', include(router.urls))
]
