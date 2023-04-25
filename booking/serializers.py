from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('booking_id', 'client_id', 'hotel_id', 'start_date', 'end_date', 'booked_rooms', 'total_price',
                  'payment_date', 'payment_method', 'unread')
