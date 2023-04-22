from rest_framework import viewsets
from .serializers import HotelSerializer
from .models import Hotel


class HotelViewSets(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


