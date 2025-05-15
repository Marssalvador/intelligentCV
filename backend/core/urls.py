from rest_framework import routers
from django.urls import path, include
from .views import CandidateCVViewSet

router = routers.DefaultRouter()
router.register(r'cvs', CandidateCVViewSet)

urlpatterns = [
    path('', include(router.urls)),
]