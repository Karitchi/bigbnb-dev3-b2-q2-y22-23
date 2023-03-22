from django.db import models
from .hotel import HotelHandler


class Hotel:
    objects = HotelHandler()

    def __init__(self):
        self.hotel_id: int = None
        self.hotel_owner_id: int = None
        self.name: str = None
        self.image = None
        self.description: str = None
        self.city_id: int = None
        self.room_quantity: int = None
        self.price: float = None

    def save(self):
        if self.hotel_id is not None:
            self.objects.update(self)
        else:
            self.objects.insert(self)

    def delete(self):
        self.objects.delete(self)
