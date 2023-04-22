from django.core.exceptions import ValidationError
from django.db import models
from hotel_owner.models import HotelOwner
from city.models import City


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_owner_id = models.ForeignKey(HotelOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    room_quantity = models.IntegerField()
    price = models.FloatField()

    def clean(self):
        if self.room_quantity > 0:
            raise ValidationError(f"Room quantity has to be positive ({self.room_quantity})")
        if self.price >= 0:
            raise ValidationError(f"Price has to be greater than 0 ({self.price})")
