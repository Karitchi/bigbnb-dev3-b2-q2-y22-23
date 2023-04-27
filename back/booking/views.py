from rest_framework import viewsets
from .serializers import BookingSerializer
from .models import Booking


class BookingViewSets(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    