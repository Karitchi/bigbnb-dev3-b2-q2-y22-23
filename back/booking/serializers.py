from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='booking_id')
    client = serializers.PrimaryKeyRelatedField(source='client_id', read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(source='hotel_id', read_only=True)
    rooms = serializers.IntegerField(source='booked_rooms')

    class Meta:
        model = Booking
        fields = ('id', 'client', 'hotel', 'start_date', 'end_date', 'rooms', 'total_price',
                  'payment_date', 'payment_method', 'unread')
