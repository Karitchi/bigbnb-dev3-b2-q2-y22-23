from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.Serializer):
    hotel_id = serializers.IntegerField(read_only=True)
    hotel_owner_id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=30)
    image = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    city_id = serializers.IntegerField(required=True)
    room_quantity = serializers.IntegerField(required=True)
    price = serializers.FloatField(required=True)

    def create(self, validated_data):
        hotel = Hotel()
        hotel.hotel_id = validated_data.get("hotel_id")
        hotel.hotel_owner_id = validated_data.get("hotel_owner_id")
        hotel.name = validated_data.get("name")
        hotel.image = validated_data.get("image")
        hotel.description = validated_data.get("description")
        hotel.city_id = validated_data.get("city_id")
        hotel.room_quantity = validated_data.get("room_quantity")
        hotel.price = validated_data.get("price")
        hotel.save()
        return hotel

    def update(self, hotel: Hotel, validated_data):
        hotel.hotel_id = validated_data.get("hotel_id", hotel.hotel_id)
        hotel.hotel_owner_id = validated_data.get("hotel_owner_id", hotel.hotel_owner_id)
        hotel.name = validated_data.get("name", hotel.name)
        hotel.image = validated_data.get("image", hotel.image)
        hotel.description = validated_data.get("description", hotel.description)
        hotel.city_id = validated_data.get("city_id", hotel.city_id)
        hotel.room_quantity = validated_data.get("room_quantity", hotel.room_quantity)
        hotel.price = validated_data.get("price", hotel.price)
        hotel.save()
        return hotel
