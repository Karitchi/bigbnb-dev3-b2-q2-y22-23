from gettext import translation
from rest_framework import viewsets
from .serializers import FacilitySerializer
from .models import Facility, Hotel
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
@api_view(['GET', 'POST'])
def facilities(request,hotel_id):
    if request.method == 'GET':
        queryset = Facility.objects.filter(hotel_id = hotel_id)
        serializer = FacilitySerializer(queryset, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        try:
            hotel_instance = get_object_or_404(Hotel, hotel_id=hotel_id)
        except Hotel.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FacilitySerializer(data=request.data, partial=True)
        if serializer.is_valid():
            facility = serializer.save(hotel_id=hotel_instance)
            serializer = FacilitySerializer(facility)  # Serialize the saved facility
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)