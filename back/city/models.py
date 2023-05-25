from django.db import models


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=25)
    location_x = models.FloatField()
    location_y = models.FloatField()
