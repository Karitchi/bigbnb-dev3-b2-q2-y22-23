from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from client.models import Client
from client.serializers import ClientSerializer


@api_view(['GET', 'POST'])
def all_clients(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        return Response(ClientSerializer(clients, many=True).data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['GET', 'DELETE'])
def client_details(request, client_id):
    try:
        client = Client.objects.all().get(pk=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(ClientSerializer(client).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_200_OK)
