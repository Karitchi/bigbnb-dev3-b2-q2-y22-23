from rest_framework import viewsets
from .serializers import CitySerializers
from .models import City


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers
