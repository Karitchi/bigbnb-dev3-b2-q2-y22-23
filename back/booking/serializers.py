from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.IntegerField(source='client_id_id')
    hotel = serializers.IntegerField(source='hotel_id_id')
    rooms = serializers.IntegerField(source='booked_rooms')

    class Meta:
        model = Booking
        fields = ('client', 'hotel', 'start_date', 'end_date', 'rooms','total_price', 'payment_date', 'payment_method', 'unread')


def data_from_booking(booking: Booking) -> dict[str:object]:
    return {
        'client': booking.client_id,
        'hotel': booking.hotel_id,
        'start_date': booking.start_date,
        'end_date': booking.end_date,
        'rooms': booking.booked_rooms,
        'total_price': booking.total_price,
        'payment_date': booking.payment_date,
        'payment_method': booking.payment_method,
        'unread': booking.unread
    }
