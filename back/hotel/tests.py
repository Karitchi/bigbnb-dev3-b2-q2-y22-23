from big_b_n_b.tests_utils import BigBNBTestCase
from . import views


class TestEndpoints(BigBNBTestCase):
    def test_all_get(self):
        request = self.factory.get('/hotels/')
        response = views.all_hotels(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))

    def test_all_post(self):
        request = self.factory.post('/hotels/', self.get_new_hotel_json())
        response = views.all_hotels(request)
        self.assertEqual(response.status_code, 201)

    def test_details_get(self):
        request = self.factory.get('/hotels/')
        response = views.hotel_detail(request, hotel_id=self.hotel.hotel_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.get_hotel_json())

        response = views.hotel_detail(request, hotel_id=-45154)
        self.assertEqual(response.status_code, 404)

    def test_details_delete(self):
        request = self.factory.delete('/hotels/')
        response = views.hotel_detail(request, hotel_id=self.hotel.hotel_id)
        self.assertEqual(response.status_code, 204)

        request = self.factory.get('/hotels/')
        response = views.hotel_detail(request, hotel_id=self.hotel.hotel_id)
        self.assertEqual(response.status_code, 404)


class HotelFilterTestCase(BigBNBTestCase):
    __url = 'localhost:8000'

    def test_filter_basic(self):
        price_min = 0
        price_max = 10000

        request = self.factory.get(
            f'http://{self.__url}/filter_hotels/?min_price={price_min}&max_price={price_max}', content_type='application/json')
        content_type = request.headers.get('Content-Type')
        response = views.filter_hotels(request)
        self.assertEqual(content_type, 'application/json')
        data = response.data
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, 200)
        for hotel in data:
            self.assertGreaterEqual(hotel["price"], 0) and self.assertLessEqual(hotel["price"], 10000)
            self.assertNotIn('key', hotel)
            self.assertIn('id', hotel)
            self.assertIn('hotel_owner', hotel)
            self.assertIn('name', hotel)
            self.assertIn('img', hotel)
            self.assertIn('description', hotel)
            self.assertIn('city', hotel)
            self.assertIn('rooms', hotel)
            self.assertIn('price', hotel)

    def test_filter_string(self):
        price_min = -5
        price_max = 10000
        request = self.factory.get(
            f'http://{self.__url}/filter_hotels/?min_price={price_min}&max_price={price_max}')
        response = views.filter_hotels(request)
        self.assertEqual(response.status_code, 400)

    def test_filter_neg(self):
        price_min = 0
        price_max = 10000000
        request = self.factory.get(
            f'http://{self.__url}/filter_hotels/?min_price={price_min}&max_price={price_max}')
        response = views.filter_hotels(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >= 1)

    def test_filter_basic_one(self):
        price_min = 50
        price_max = 100

        request = self.factory.get(
            f'http://{self.__url}/filter_hotels/?min_price={price_min}&max_price={price_max}')
        response = views.filter_hotels(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >= 1)
        for hotel in response.data:
            self.assertGreaterEqual(hotel['price'], 50) and self.assertGreaterEqual(hotel['price'], 100)
