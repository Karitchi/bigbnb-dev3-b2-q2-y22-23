from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializer


@api_view(['GET', 'POST'])
def hotels_list(request):
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def hotel_detail(request, id):
    hotel = Hotel.objects.get(id)
    if hotel is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
