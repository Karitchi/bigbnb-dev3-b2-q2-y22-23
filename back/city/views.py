from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import City
from .serializers import CitySerializers


@api_view(['GET', 'POST'])
def all_cities(request):
    if request.method == 'GET':
        cities = City.objects.all()
        return Response(data=CitySerializers(cities, many=True).data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CitySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['GET', 'DELETE'])
def city_details(request, city_id):
    try:
        city = City.objects.all().get(pk=city_id)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(data=CitySerializers(city).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
