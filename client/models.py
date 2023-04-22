from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mail = models.CharField(max_length=250)
    password = models.CharField(max_length=15)
