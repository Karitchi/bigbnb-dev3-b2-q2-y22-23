import random
import string

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.datetime_safe import datetime
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models.fields.files import ImageField

from booking.models import Booking
from city.models import City
from client.models import Client
from hotel.models import Hotel
from hotel_owner.models import HotelOwner

User = get_user_model()


class BigBNBTestCase(TestCase):
    @staticmethod
    def date_to_string(date) -> str:
        return date.strftime('%Y-%m-%d')

    @staticmethod
    def get_random_str(length: int) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    @staticmethod
    def user_to_json(user: User) -> dict[str:any]:
        return {
            "id": user.id,
            "password": user.password,
            "last_login": user.last_login,
            "mail": user.mail,
            "name": user.name,
            "lastname": user.lastname,
            "is_active": user.is_active,
            "staff": user.staff,
            "admin": user.admin
        }

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

        self.city = City.objects.create(name="Ottignies", country="Beliguqe", location_x=100, location_y=100)
        self.hotel_owner_user = User.objects.create_user(
            mail="test@mail.com",
            lastname="Tim",
            name="Dupont",
            password="mon_mpd"
        )
        self.hotel_owner_obj = HotelOwner.objects.create(user_id=self.hotel_owner_user.id, society_name="Ibis")

        self.client_user = User.objects.create_user(
            mail="jean@mail.com",
            lastname="Jean",
            name="Doo",
            password="password"
        )
        self.client_obj = Client.objects.create(user_id=self.client_user.id)

        self.hotel = Hotel.objects.create(
            name="Novhotel",
            description="Un bel hôtel",
            room_quantity=100,
            price=10,
            hotel_owner_id=self.hotel_owner_obj,
            city_id=self.city
        )

        self.booking = Booking.objects.create(
            start_date=datetime.now(),
            end_date=datetime.now(),
            booked_rooms=10,
            total_price=100,
            payment_date=datetime.now(),
            payment_method="paypal",
            client_id=self.client_obj,
            hotel_id=self.hotel
        )

    def get_new_booking_json_post(self) -> dict[str:any]:
        return {
            "client": self.client_obj.user_id,
            "hotel": self.hotel.hotel_id,
            "start_date": "2023-05-19",
            "end_date": "2023-05-20",
            "rooms": 100,
            "total_price": 100.0,
            "payment_date": "2023-05-21",
            "payment_method": "pauypal",
        }

    def get_booking_json(self) -> dict[str:any]:
        return {
            "id": self.booking.booking_id,
            "client": self.booking.client_id.user_id,
            "hotel": self.booking.hotel_id.hotel_id,
            "start_date": self.date_to_string(self.booking.start_date),
            "end_date": self.date_to_string(self.booking.end_date),
            "rooms": self.booking.booked_rooms,
            "total_price": self.booking.total_price,
            "payment_date": self.date_to_string(self.booking.payment_date),
            "payment_method": self.booking.payment_method,
            "unread": self.booking.unread,
            "approved": self.booking.approved
        }

    @staticmethod
    def get_new_city_json() -> dict[str:any]:
        return {
            "name": "Limelette",
            "country": "Belgique",
            "location_x": 300,
            "location_y": -100.0
        }

    def get_city_json(self) -> dict[str:any]:
        return {
            "id": self.city.city_id,
            "name": self.city.name,
            "country": self.city.country,
            "location_x": self.city.location_x,
            "location_y": self.city.location_y
        }

    def get_new_hotel_json(self) -> dict[str:any]:
        return {
            "hotel_owner": self.hotel_owner_obj.user_id,
            "name": "Ibis",
            "description": "Un bel hôtel\nÇa rime",
            "city": self.city.city_id,
            "rooms": 100,
            "price": 99.99
        }

    def get_hotel_json(self) -> dict[str:any]:
        return {
            "id": self.hotel.hotel_id,
            "hotel_owner": self.hotel.hotel_owner_id.user_id,
            "name": self.hotel.name,
            "img": None,
            "description": self.hotel.description,
            "city": self.hotel.city_id.city_id,
            "rooms": self.hotel.room_quantity,
            "price": self.hotel.price
        }

    @staticmethod
    def get_new_client_json() -> dict[str:any]:
        return {
            "info": BigBNBTestCase.get_new_user_json()
        }

    @staticmethod
    def get_new_hotel_owner_json() -> dict[any:str]:
        return {
            "info": BigBNBTestCase.get_new_user_json(),
            "company": BigBNBTestCase.get_random_str(10)
        }

    @staticmethod
    def get_auth_user_json(user: User) -> dict[str:any]:
        return {
            "id": user.id,
            "password": user.password,
            "mail": user.mail,
            "name": user.name,
            "lastname": user.lastname,
            "last_login": user.last_login,
            "is_active": user.is_active,
            "staff": user.staff,
            "admin": user.admin

               } | BigBNBTestCase.get_not_auth_user_json(user)

    @staticmethod
    def get_not_auth_user_json(user: User) -> dict[str:any]:
        return {
            "id": user.id,
            "mail": user.mail,
            "name": user.name,
            "lastname": user.lastname
        }

    def get_auth_client_json(self) -> dict[str:any]:
        return {
            'id': self.client_obj.user_id,
            'info': self.get_auth_user_json(self.client_user)
        }

    def get_not_auth_client_json(self) -> dict[str:any]:
        json = self.get_auth_client_json()
        json['info'] = self.get_not_auth_user_json(self.client_user)
        return json

    def get_auth_hotel_owner_json(self) -> dict[str:any]:
        return {
            'id': self.hotel_owner_obj.user_id,
            'company': self.hotel_owner_obj.society_name,
            'info': self.get_auth_user_json(self.hotel_owner_user)
        }

    def get_not_auth_hotel_owner_json(self) -> dict[str:any]:
        json = self.get_auth_hotel_owner_json()
        json['info'] = self.get_not_auth_user_json(self.hotel_owner_user)
        return json

    @staticmethod
    def get_user_body_for_token(user: User) -> dict[str:str]:
        return {
            'mail': user.mail,
            'password': user.password
        }

    @staticmethod
    def get_token(user: User) -> str:
        return str(RefreshToken.for_user(user).access_token)

    @staticmethod
    def add_auth_token_to_request(request, user):
        request.META['HTTP_AUTHORIZATION'] = BigBNBTestCase.get_token(user)
        return request

    @staticmethod
    def get_new_user_json() -> dict[str:any]:
        return {
            'mail': f"{BigBNBTestCase.get_random_str(5)}@mail.com",
            'lastname': BigBNBTestCase.get_random_str(5),
            'name': BigBNBTestCase.get_random_str(5),
            'password': BigBNBTestCase.get_random_str(5)
        }
