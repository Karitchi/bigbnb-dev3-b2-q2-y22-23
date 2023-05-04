from rest_framework import generics, viewsets
from .serializers import HotelSerializer
from .models import Hotel


class HotelViewSets(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelListAPIView(generics.ListAPIView):
    serializer_class = HotelSerializer

    def get_queryset(self):
        queryset = Hotel.objects.all()

        # Filter by maximum and minimum price
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        # Filter by minimum and maximum rating
        min_rating = self.request.query_params.get('min_rating')
        max_rating = self.request.query_params.get('max_rating')
        if min_rating is not None:
            queryset = queryset.filter(rating__gte=min_rating)
        if max_rating is not None:
            queryset = queryset.filter(rating__lte=max_rating)

        return queryset
