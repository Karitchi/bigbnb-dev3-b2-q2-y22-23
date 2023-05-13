from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    hotel_owner = serializers.IntegerField(source='hotel_owner_id_id')
    city = serializers.IntegerField(source='city_id_id')
    rooms = serializers.IntegerField(source='room_quantity')

    class Meta:
        model = Hotel
        fields = ('hotel_owner', 'name', 'description', 'city', 'rooms', 'price')
