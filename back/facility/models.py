from django.db import models
from hotel.models import Hotel

# Create your models here.
class Facility(models.Model):
    facility_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
