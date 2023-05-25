from rest_framework import viewsets
from .serializers import ClientReviewSerializer
from .models import ClientReview
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
class ClientReviewViewSet(viewsets.ModelViewSet):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerializer

@api_view(['GET', 'POST'])
def hotel_review_list(request, hotel_id):
    if request.method == 'GET':
        queryset = ClientReview.objects.filter(hotel_id=hotel_id)
        serializer = ClientReviewSerializer(queryset, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ClientReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)