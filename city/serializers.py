from rest_framework import serializers
from .models import City


class CitySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('city_id', 'name', 'country', 'location_x', 'location_y')
