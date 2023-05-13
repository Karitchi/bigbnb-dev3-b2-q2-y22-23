from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Hotel
from .serializers import HotelSerializer
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


@api_view(['GET', 'DELETE', 'PATCH'])
def hotel_detail(request, hotel_id):
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(HotelSerializer(hotel).data)

    if request.method == 'PATCH':
        if len(request.data['image']) > 100:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if len(request.data['name']) < 3 or len(request.data['name']) > 100:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if request.data['price'] <= '0':
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = HotelSerializer(hotel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
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