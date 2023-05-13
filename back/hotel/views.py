from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .serializers import HotelSerializer
from .models import Hotel
from image.models import Image
from image.serializers import ImageSerializer


@api_view(['GET', 'POST'])
def all_hotels(request):
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def hotel_detail(request, hotel_id):
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(HotelSerializer(hotel).data)

    if request.method == 'PUT':
        serializer = HotelSerializer(hotel, data=request.data)
        request.data['id'] = hotel.hotel_id
        request.data['rooms'] = hotel.room_quantity
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def hotel_images(request, hotel_id):

    try:
        images = Image.objects.filter(hotel_id=hotel_id)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)