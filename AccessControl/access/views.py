from django.shortcuts import render

from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Door, Person, AccessLog
from .serializers import DoorSerializer, PersonSerializer, AccessLogSerializer


class RealTimeAccessLogView(TemplateView):
    template_name = 'access/realtime.html'
    
class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer