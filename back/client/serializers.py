from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import empty

from user.serializers import UserSerializer, SimpleUserSerializer
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user_id', required=False)
    info = serializers.SerializerMethodField()
    __full_info = False

    def __init__(self, instance=None, data=empty, full_info=None, **kwargs, ):
        super().__init__(instance=instance, data=data, **kwargs)
        self.__full_info = full_info

    class Meta:
        model = Client
        fields = ['id', 'info']

    def get_info(self, client):
        selected_user = get_user_model().objects.filter(id=client.user_id)[0]
        if self.__full_info:
            return UserSerializer(selected_user).data
        return SimpleUserSerializer(selected_user).data
