from django.urls import path
from .consumers import AccessLogConsumer

websocket_urlpatterns = [
    path('ws/access_logs/', AccessLogConsumer.as_asgi()),
]
