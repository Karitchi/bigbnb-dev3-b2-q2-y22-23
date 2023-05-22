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
