from django.db import models
from client.models import Client
from hotel.models import Hotel


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booked_rooms = models.IntegerField()
    total_price = models.FloatField()
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20)
    unread = models.BooleanField(default=True)
    approved = models.BooleanField(null=True)
