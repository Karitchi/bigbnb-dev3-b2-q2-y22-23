from django.db.models import Min, Max, Avg
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from city.models import City
from .models import Hotel
from .serializers import HotelSerializer


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
        if 'img' in request.data.keys() and len(request.data['img']) > 100:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if len(request.data['name']) < 3 or len(request.data['name']) > 100:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if request.data['price'] <= 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = HotelSerializer(hotel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def filter_hotels(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_room = request.GET.get('min_room')
    max_room = request.GET.get('max_room')

    try:
        min_price = float(min_price)
        max_price = float(max_price)
        min_room = int(min_room)
        max_room = int(max_room)
        if min_price < 0 or max_price < min_price:
            raise ValueError
        if min_room < 0 or max_room < min_room:
            raise ValueError

    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    hotels = Hotel.objects.all()
    hotels = hotels.filter(price__gte=min_price)
    hotels = hotels.filter(price__lte=max_price)
    hotels = hotels.filter(room_quantity__gte=min_room)
    hotels = hotels.filter(room_quantity__lte=max_room)
    serializer = HotelSerializer(hotels, many=True)
    return Response(status=status.HTTP_200_OK, data=serializer.data)
