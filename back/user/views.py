from abc import ABC

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from client.models import Client
from hotel_owner.models import HotelOwner


class UserTokenPairSerializer(TokenObtainPairSerializer):
    @staticmethod
    def get_user_type(user_id: int) -> str | None:
        try:
            Client.objects.all().get(pk=user_id)
            return 'client'
        except Client.DoesNotExist:
            try:
                HotelOwner.objects.all().get(pk=user_id)
                return 'hotel_owner'
            except HotelOwner.DoesNotExist:
                return None

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.id
        token['type'] = UserTokenPairSerializer.get_user_type(user.id)
        return token


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenPairSerializer
