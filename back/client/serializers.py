from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='client_id', required=False)

    class Meta:
        model = Client
        fields = ('id', 'name', 'lastname', 'mail', 'password')
