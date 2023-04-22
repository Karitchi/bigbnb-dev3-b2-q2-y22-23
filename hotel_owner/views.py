from rest_framework import viewsets
from .serializers import HotelOwnerSerializer
from .models import HotelOwner


class HotelOwnerViewSet(viewsets.ModelViewSet):
    queryset = HotelOwner.objects.all()
    serializer_class = HotelOwnerSerializer
