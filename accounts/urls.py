from django.urls import path, include
from rest_framework import routers
from accounts.views import CustomerApiV1ViewSet, SallerApiV1ViewSet

app_name = 'accounts'

router = routers.SimpleRouter()
router.register('customer', CustomerApiV1ViewSet, basename='customer')
router.register('saller', SallerApiV1ViewSet, basename='saller')

urlpatterns = [
    path('', include(router.urls))
]
