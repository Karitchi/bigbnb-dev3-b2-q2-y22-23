from rest_framework import viewsets
from user.models import User
from user.serializers import UserSerializer


class UserViews(viewsets.ModelViewSet):
    queryset = User.object.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
