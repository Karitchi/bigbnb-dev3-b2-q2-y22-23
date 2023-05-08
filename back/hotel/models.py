from django.core.exceptions import ValidationError
from django.db import models
from hotel_owner.models import HotelOwner
from city.models import City


def name_file(self, filename):
    return '/'.join(['images', str(self.name), filename])


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_owner_id = models.ForeignKey(HotelOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=name_file)
    description = models.TextField()
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    room_quantity = models.IntegerField()
    price = models.FloatField()
