from django.db import connection


class HotelHandler:
    def __init__(self):
        pass

    @staticmethod
    def format_boolean(value: bool) -> str:
        return 'TRUE' if value else 'FALSE'

    @staticmethod
    def format_date(value):
        return value.isoformat()

    @staticmethod
    def format_datetime(value):
        return value.isoformat()

    @staticmethod
    def update(hotel):
        cursor = connection.cursor()
        query = """
        SET hotel_owner_id='{0}',
            name='{1},
            image='{2}',
            description='{3}',
            city_id='{4}',
            room_quantity='{5}',
            price='{6}',
        WHERE hotel_id='{7}'
        """.format(
            hotel.hotel_owner_id,
            hotel.name,
            hotel.image,
            hotel.description,
            hotel.city_id,
            hotel.room_quantity,
            hotel.price,
            hotel.id
        )
        cursor.execute(query)

    @staticmethod
    def insert(hotel):
        cursor = connection.cursor()
        query = """
        INSERT INTO hotel (hotel_id, hotel_owner_id, name, image, description, city_id, room_quantity, price)
        VALUES (DEFAULT, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')
        """.format(
            hotel.hotel_owner_id,
            hotel.name,
            hotel.image,
            hotel.description,
            hotel.city_id,
            hotel.room_quantity,
            hotel.price
        )
        cursor.execute(query)

    @staticmethod
    def all():
        cursor = connection.cursor()
        query = """
        SELECT hotel_id, hotel_owner_id, name, image, description, city_id, room_quantity, price
        FROM hotel
        """
        cursor.execute(query)

        from .models import Hotel
        hotels: list[Hotel] = []
        for row in cursor.fetchall():
            hotel: Hotel = Hotel()
            hotel.hotel_id = row[0]
            hotel.hotel_owner_id = row[1]
            hotel.name = row[2]
            hotel.image = row[3]
            hotel.description = row[4]
            hotel.city_id = row[5]
            hotel.room_quantity = row[6]
            hotel.price = row[7]
            hotels.append(hotel)

        return hotels

    @staticmethod
    def get(hotel_id: int):
        cursor = connection.cursor()
        query = """
                SELECT hotel_id, hotel_owner_id, name, image, description, city_id, room_quantity, price
                FROM hotel
                WHERE hotel_id='{0}'
                """.format(hotel_id)
        cursor.execute(query)
        hotels = []

        from .models import Hotel
        for row in cursor.fetchall():
            hotel: Hotel = Hotel()
            hotel.hotel_id = row[0]
            hotel.hotel_owner_id = row[1]
            hotel.name = row[2]
            hotel.image = row[3]
            hotel.description = row[4]
            hotel.city_id = row[5]
            hotel.room_quantity = row[6]
            hotel.price = row[7]
            return hotel
        return None
