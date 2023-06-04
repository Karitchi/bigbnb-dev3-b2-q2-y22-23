from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='hotel_id', required=False)
    hotel_owner = serializers.IntegerField(source='hotel_owner_id_id')
    city = serializers.IntegerField(source='city_id_id')
    rooms = serializers.IntegerField(source='room_quantity')
    img = serializers.ImageField(source='image', required=False)

    class Meta:
        model = Hotel
        fields = ('id', 'hotel_owner', 'name', 'img', 'description', 'city', 'rooms', 'price', 'mail', 'phone_number')
        # fields = ('hotel_owner', 'name', 'description', 'city', 'rooms', 'price')
