from rest_framework import serializers

from user.serializers import TypeUserSerializer
from .models import Client


class ClientSerializer(TypeUserSerializer):
    id = serializers.IntegerField(source='user_id', required=False)
    info = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'info']
