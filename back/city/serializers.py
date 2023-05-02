from rest_framework import serializers
from .models import City


class CitySerializers(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='city_id')

    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'location_x', 'location_y')
