from rest_framework import serializers
from .models import HotelOwner


class HotelOwnerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='hotel_owner_id')
    company = serializers.CharField(source='society_name')

    class Meta:
        model = HotelOwner
        fields = ('id', 'name', 'lastname', 'company', 'mail', 'password')
