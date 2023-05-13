from django.db import models
from hotel.models import Hotel

# Create your models here.
class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    url = models.ImageField(upload_to="hotels")