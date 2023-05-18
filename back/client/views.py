from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from client.models import Client
from client.serializers import ClientSerializer
from django.contrib.auth import get_user_model

from user.serializers import UserSerializer, UserSerializerValidator

User = get_user_model()


@api_view(['GET', 'POST'])
def all_clients(request) -> Response:
    if request.method == 'GET':
        clients = Client.objects.select_related('user').all()
        return Response(ClientSerializer(clients, many=True).data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        validator: UserSerializerValidator = UserSerializerValidator(data=request.data)
        if not validator.is_valid():
            return validator.get_current_response()

        validator.create_user()
        data = validator.get_final_data()
        client_serializer = ClientSerializer(data=data)
        if not client_serializer.is_valid():
            return Response(data=client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        client_serializer.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def client_details(request, client_id) -> Response:
    try:
        client = Client.objects.all().get(pk=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(ClientSerializer(client).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        User.objects.filter(id=client.user_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
