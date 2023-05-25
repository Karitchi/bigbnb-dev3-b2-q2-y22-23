from big_b_n_b.tests_utils import BigBNBTestCase
from . import views
from rest_framework.test import force_authenticate, APIClient


class TestEndpoints(BigBNBTestCase):
    def test_all_get(self):
        request = self.factory.get('/clients/')
        response = views.all_clients(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))

    def test_all_post(self):
        client_json = self.get_new_client_json()
        request = self.factory.post('/clients/', client_json, format='json')
        response = views.all_clients(request)
        self.assertEqual(response.status_code, 201)

        request = self.factory.post('/clients/', client_json, format='json')
        response = views.all_clients(request)
        self.assertEqual(response.status_code, 409)

        request = self.factory.post('/clients/', {"client": "info"}, format='json')
        response = views.all_clients(request)
        self.assertEqual(response.status_code, 400)

    def test_details_auth_get(self):
        request = self.factory.get('/clients/')
        self.add_auth_token_to_request(request, self.client_user)
        response = views.client_details(request, client_id=self.client_obj.user_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.get_auth_client_json())

        response = views.client_details(request, client_id=-161654)
        self.assertEqual(response.status_code, 404)

    def test_details_not_auth_get(self):
        request = self.factory.get('/clients/')
        response = views.client_details(request, client_id=self.client_obj.user_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.get_not_auth_client_json())

        response = views.client_details(request, client_id=-45642)
        self.assertEqual(response.status_code, 404)

    def test_details_delete(self):
        request = self.factory.delete('/clients/')
        response = views.client_details(request, client_id=self.client_obj.user_id)
        self.assertEqual(response.status_code, 401)

        self.add_auth_token_to_request(request, self.client_user)
        response = views.client_details(request, client_id=self.client_obj.user_id)
        self.assertEqual(response.status_code, 204)

        request = self.factory.get('/clients/')
        response = views.client_details(request, client_id=self.client_obj.user_id)
        self.assertEqual(response.status_code, 404)
