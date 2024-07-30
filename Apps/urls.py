from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RamaisViewSet

router = DefaultRouter()
router.register(r'ramais', RamaisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
