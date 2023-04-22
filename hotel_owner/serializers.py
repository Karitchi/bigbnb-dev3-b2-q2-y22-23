from rest_framework import serializers
from .models import HotelOwner


class HotelOwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HotelOwner
        fields = ('hotel_owner_id', 'name', 'lastname', 'society_name', 'mail', 'password')
