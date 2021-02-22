from rest_framework import serializers
from event.models import Event

class EventSerializers(serializers.ModelSerializer):
    organiser = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Event
        fields=('name','category','image','start_date','end_date','vanue','maximum_participants','description','slug','slot_booked','organiser','create_date')

class EventCreateSerializers(serializers.ModelSerializer):
    organiser = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model= Event
        fields=('name','category','image','start_date','end_date','vanue','maximum_participants','description')
