from rest_framework import serializers

from user.serializers import TypeUserSerializer
from .models import HotelOwner


class HotelOwnerSerializer(TypeUserSerializer):
    id = serializers.IntegerField(source='user_id', required=False)
    company = serializers.CharField(source='society_name')
    info = serializers.SerializerMethodField()

    class Meta:
        model = HotelOwner
        fields = ('id', 'company', 'info')
