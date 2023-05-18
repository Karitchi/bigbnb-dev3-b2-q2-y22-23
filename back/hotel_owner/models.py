from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class HotelOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='user_id')
    society_name = models.CharField(max_length=50)
