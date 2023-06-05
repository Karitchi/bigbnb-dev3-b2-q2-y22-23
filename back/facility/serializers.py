from rest_framework import serializers
from .models import Facility, Hotel


# class FacilitySerializer(serializers.ModelSerializer):
class FacilitySerializer(serializers.ModelSerializer):
    hotel_id_id = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all(), source='hotel_id')

    class Meta:
        model = Facility
        fields = ['name', 'description', 'hotel_id_id']
