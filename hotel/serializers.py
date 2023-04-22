from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_id', 'hotel_owner_id', 'name', 'image', 'description', 'city_id', 'room_quantity', 'price')
