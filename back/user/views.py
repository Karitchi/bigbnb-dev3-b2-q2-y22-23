import json
from abc import ABC

import jwt
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


def decode_jwt_from_request(request) -> dict[str:any]:
    if 'HTTP_AUTHORIZATION' not in request.META.keys():
        raise ValueError('Not authorization')

    from big_b_n_b.settings import SIMPLE_JWT
    return jwt.decode(
        request.META['HTTP_AUTHORIZATION'],
        algorithms=SIMPLE_JWT['ALGORITHM'],
        options={'verify_signature': False}
    )


def is_user_authorized(request, user_id: int) -> bool:
    try:
        return decode_jwt_from_request(request)['user_id'] == user_id
    except ValueError:
        return False
