# Модуль API URLS проекта.
from django.urls import include, path
from rest_framework import routers

from .views import DonationViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('donations', DonationViewSet, basename='donations')

urlpatterns = [
    path('', include(router_v1.urls)),
]
