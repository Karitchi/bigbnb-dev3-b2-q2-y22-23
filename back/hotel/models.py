from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from city.models import City
from client.models import Client
from hotel_owner.models import HotelOwner


def name_file(self, filename):
    return '/'.join(['images', str(self.name), filename])


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_owner_id = models.ForeignKey(HotelOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=name_file)
    description = models.TextField(null=True, blank=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    room_quantity = models.IntegerField()
    price = models.FloatField()


class HotelRating(models.Model):
    hotel_id = models.ForeignKey(Hotel, primary_key=True, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.SET_NULL,null=True)
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        unique_together = (('hotel_id', 'client_id'),)
