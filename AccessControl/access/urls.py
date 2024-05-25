# access/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoorViewSet, PersonViewSet, AccessLogViewSet
from .views import RealTimeAccessLogView


router = DefaultRouter()
router.register(r'doors', DoorViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'access_logs', AccessLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('realtime/', RealTimeAccessLogView.as_view(), name='realtime'),
]