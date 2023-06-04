from big_b_n_b.tests_utils import BigBNBTestCase
from . import views


class TestEndpoints(BigBNBTestCase):
    def test_all_get(self):
        request = self.factory.get('/cities/')
        response = views.all_cities(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))

    def test_all_post(self):
        request = self.factory.post('/cities/', self.get_new_city_json(), format='json')
        response = views.all_cities(request)
        self.assertEqual(response.status_code, 201)

    def test_details_get(self):
        request = self.factory.get('/cities/')
        response = views.city_details(request, city_id=self.city.city_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.get_city_json())

        response = views.city_details(request, city_id=-45164)
        self.assertEqual(response.status_code, 404)

    def test_details_delete(self):
        request = self.factory.delete('/cities/')
        response = views.city_details(request, city_id=self.city.city_id)
        self.assertEqual(response.status_code, 204)

        request = self.factory.get('/cities/')
        response = views.city_details(request, city_id=self.city.city_id)
        self.assertEqual(response.status_code, 404)
