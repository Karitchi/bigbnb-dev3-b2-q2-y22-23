from django.db import models
from client.models import Client
from hotel.models import Hotel
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ClientReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])