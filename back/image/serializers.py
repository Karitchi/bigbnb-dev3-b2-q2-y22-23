from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    hotel_id = serializers.IntegerField(source='hotel_id_id')

    class Meta:
        model = Image
        fields = ('image_id', 'hotel_id', 'url')
