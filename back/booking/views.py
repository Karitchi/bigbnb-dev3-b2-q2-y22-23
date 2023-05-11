from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BookingSerializer, data_from_booking
from .models import Booking


@api_view(['GET', 'POST'])
def all_bookings(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        return Response(BookingSerializer(bookings, many=True).data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['GET', 'DELETE'])
def bookings_details(request, booking_id):
    try:
        booking = Booking.objects.all().get(pk=booking_id)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(BookingSerializer(booking).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        booking.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['PATCH'])
def set_read(request, booking_id):
    print(request.data)
    try:
        booking = Booking.objects.all().get(pk=booking_id)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if 'unread' not in request.data.keys():
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)

    serializer = BookingSerializer(booking, data={'unread': request.data['unread']}, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def set_approved(request, booking_id):
    try:
        booking = Booking.objects.all().get(pk=booking_id)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if 'approved' not in request.data.keys():
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)

    serializer = BookingSerializer(booking, data={'approved': request.data['approved']}, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
