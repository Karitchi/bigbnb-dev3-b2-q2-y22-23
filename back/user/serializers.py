from rest_framework import serializers, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'mail', 'name', 'lastname')


class UserSerializerValidator:
    __data = None
    __serializer = None
    __error = False

    def __init__(self, data: dict):
        self.__data = data
        if 'info' in data.keys():
            data = data['info']

        self.__serializer = UserSerializer(data=data)
        if not self.__serializer.is_valid():
            self.__error = self.__serializer.errors
        else:
            self.__is_valid = True

    def is_valid(self) -> bool:
        return self.__error is not None

    def create_user(self):
        if not self.is_valid():
            raise RuntimeError('Data invalide')
        user = User.objects.create_user_from_dict(self.__serializer.data)
        self.__data['id'] = user.id
        return user

    def get_final_data(self) -> dict:
        if not self.is_valid():
            raise RuntimeError('Data invalide')
        if 'id' not in self.__data:
            raise RuntimeError('User not created yet, use `user#create_user()`')

        data = {
            'id': self.__data['id'],
            'info': self.__data
        }
        if 'company' not in self.__data.keys():
            return data
        data['company'] = self.__data['company']
        return data

    def get_current_response(self) -> Response:
        if self.is_valid():
            return Response(data=self.get_final_data(), status=status.HTTP_200_OK)
        return Response(data=self.__error, status=status.HTTP_400_BAD_REQUEST)


