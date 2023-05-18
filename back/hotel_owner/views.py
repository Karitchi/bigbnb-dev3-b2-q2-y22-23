from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from user.serializers import UserSerializer, UserSerializerValidator
from .serializers import HotelOwnerSerializer
from .models import HotelOwner


User = get_user_model()


@api_view(['GET', 'POST'])
def all_hotel_owners(request) -> Response:
    if request.method == 'GET':
        hotel_owners = HotelOwner.objects.select_related('user').all()
        return Response(HotelOwnerSerializer(hotel_owners, many=True).data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        validator: UserSerializerValidator = UserSerializerValidator(data=request.data)
        if not validator.is_valid():
            return validator.get_current_response()

        validator.create_user()
        hotel_owner_serializer = HotelOwnerSerializer(data=validator.get_final_data())
        if not hotel_owner_serializer.is_valid():

            return Response(data=hotel_owner_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        hotel_owner_serializer.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def hotel_owner_detail(request, hotel_owner_id):
    try:
        hotel_owner = HotelOwner.objects.get(pk=hotel_owner_id)
    except HotelOwner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(HotelOwnerSerializer(hotel_owner).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        User.objects.filter(id=hotel_owner.user_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
