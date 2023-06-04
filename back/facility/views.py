from rest_framework import viewsets
from .serializers import FacilitySerializer
from .models import Facility
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
@api_view(['GET'])
def facilities(request,hotel_id):
    if request.method == 'GET':
        queryset = Facility.objects.filter(hotel_id = hotel_id)
        serializer = FacilitySerializer(queryset, many=True)
        return Response(serializer.data)