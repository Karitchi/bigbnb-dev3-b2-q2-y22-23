import uuid

from django.db.models import Min, Max, Avg
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from city.models import City
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
    location = request.GET.get('location')
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

    hotels = Hotel.objects.filter(city_id__name__icontains=location)
    hotels = hotels.filter(price__gte=min_price)
    hotels = hotels.filter(price__lte=max_price)
    hotels = hotels.filter(room_quantity__gte=min_room)
    hotels = hotels.filter(room_quantity__lte=max_room)
    serializer = HotelSerializer(hotels, many=True)
    return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(['GET', 'POST'])
def hotel_images(request, hotel_id):
    try:
        images = Image.objects.filter(hotel_id=hotel_id)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        image_file = request.FILES.get('image')
        image_file.name = str(uuid.uuid4()) + '.' + image_file.name.split('.')[-1]
        model = Image()
        model.url = image_file
        model.hotel_id = Hotel.objects.all().get(hotel_id=hotel_id)
        model.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def search(request):
    location: str = request.GET.get('location')
    min_price: str = request.GET.get('min_price')
    max_price: str = request.GET.get('max_price')
    min_room: str = request.GET.get('min_room')
    max_room: str = request.GET.get('max_room')

    hotels = Hotel.objects.all()
    if location is not None:
        hotels = hotels.filter(city_id__name__icontains=location)

    if min_price is not None and min_price.isdigit():
        hotels = hotels.filter(price__gte=float(min_price))

    if max_price is not None and max_price.isdigit():
        hotels = hotels.filter(price__lte=float(max_price))

    if min_room is not None and min_room.isdigit():
        hotels = hotels.filter(room_quantity__gte=int(min_room))

    if max_room is not None and max_room.isdigit():

        hotels = hotels.filter(room_quantity__lte=int(max_room))

    return Response(status=status.HTTP_200_OK, data=HotelSerializer(hotels, many=True).data)
