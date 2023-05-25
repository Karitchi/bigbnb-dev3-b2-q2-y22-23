from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from city.models import City
from client.models import Client
from hotel_owner.models import HotelOwner

class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_owner_id = models.ForeignKey(HotelOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    room_quantity = models.IntegerField()
    price = models.FloatField()