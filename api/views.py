from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import EventCreateSerializers, EventSerializers
from datetime import datetime
from event.models import Event
# Create your views here.

class EventView(generics.ListAPIView):
    now=datetime.now()
    queryset= Event.objects.filter(start_date__gte=now)
    serializer_class = EventSerializers

class AllEventsView(generics.ListAPIView):
    queryset= Event.objects.all()
    serializer_class = EventSerializers

