from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='hotel_id')
    hotel_owner = serializers.PrimaryKeyRelatedField(source='hotel_owner_id', read_only=True)
    city = serializers.PrimaryKeyRelatedField(source='city_id', read_only=True)
    rooms = serializers.IntegerField(source='room_quantity')

    class Meta:
        model = Hotel
        fields = ('id', 'hotel_owner', 'name', 'image', 'description', 'city', 'rooms', 'price', 'rating')
