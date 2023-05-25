from rest_framework import serializers, status
from django.contrib.auth import get_user_model
from rest_framework.fields import empty
from rest_framework.response import Response
from typing import Type

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'mail', 'name', 'lastname')


class TypeUserSerializer(serializers.ModelSerializer):
    __full_info: bool = False

    def __init__(self, instance=None, data=empty, full_info: bool = None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.__full_info = full_info

    def get_serializer(self, user: User) -> serializers.ModelSerializer:
        return UserSerializer(user) if self.__full_info else SimpleUserSerializer(user)

    def get_info(self, user_type_instance):
        selected_user = get_user_model().objects.filter(id=user_type_instance.user_id)[0]
        return self.get_serializer(selected_user).data


class UserSerializerValidator:
    __data = None
    __serializer = None
    __error = False
    __is_data_valid = None
    __is_duplicated = None
    __serializer_class: Type[serializers.ModelSerializer] = None
    __user: User = None

    def __init__(self, data: dict, serializer_class: Type[serializers.ModelSerializer]):
        self.__data = data
        if 'info' in data.keys():
            data = data['info']

        self.__serializer = UserSerializer(data=data)
        self.__serializer_class = serializer_class
        if not self.__serializer.is_valid():
            self.__error = self.__serializer.errors

    def is_data_valid(self) -> bool:
        if self.__is_data_valid is not None:
            return self.__is_data_valid

        if 'info' not in self.__data.keys():
            self.__is_data_valid = False
            return self.__is_data_valid

        try:
            keys = self.__data['info'].keys()
        except AttributeError:
            self.__is_data_valid = False
            return self.__is_data_valid
        self.__is_data_valid = 'mail' in keys \
                               and 'password' in keys \
                               and 'lastname' in keys \
                               and 'name' in keys \
                               and self.__error is not None
        return self.__is_data_valid

    def create_user(self) -> User:
        if not self.is_data_valid():
            raise RuntimeError('Data invalide')
        if self.is_duplicated():
            raise RuntimeError('User already exist with this mail')

        self.__user = User.objects.create_user_from_dict(self.__serializer.data)
        self.__data['id'] = self.__user.id
        return self.__user

    def is_duplicated(self) -> bool:
        if not self.is_data_valid():
            raise RuntimeError('Data invalide')

        if self.__is_duplicated is None:
            self.__is_duplicated = len(User.objects.all().filter(mail=self.__data['info']['mail'])) > 0

        return self.__is_duplicated

    def get_final_data(self) -> dict:
        if not self.is_data_valid():
            raise RuntimeError('Data invalide')
        if not self.is_user_has_been_created():
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
        if not self.is_data_valid():
            return Response(data=self.__error, status=status.HTTP_400_BAD_REQUEST)

        if self.is_duplicated():
            return Response(status=status.HTTP_409_CONFLICT)

        if not self.is_user_has_been_created():
            self.create_user()

        serializer: serializers.ModelSerializer = self.__serializer_class(data=self.get_final_data())
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def is_user_has_been_created(self) -> bool:
        return self.__user is not None

    def is_valid(self) -> bool:
        return self.is_data_valid() and not self.is_duplicated()
