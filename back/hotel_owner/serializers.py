from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.serializers import UserSerializer
from .models import HotelOwner


class HotelOwnerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='user_id', required=False)
    company = serializers.CharField(source='society_name')
    info = serializers.SerializerMethodField()

    class Meta:
        model = HotelOwner
        fields = ('id', 'company', 'info')

    @staticmethod
    def get_info(hotel_owner):
        selected_user = get_user_model().objects.filter(id=hotel_owner.user_id)[0]
        return UserSerializer(selected_user).data
