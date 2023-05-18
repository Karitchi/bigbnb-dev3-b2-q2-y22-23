from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user_id', required=False)
    info = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'info']

    @staticmethod
    def get_info(client):
        selected_user = get_user_model().objects.filter(id=client.user_id)[0]
        return UserSerializer(selected_user).data
