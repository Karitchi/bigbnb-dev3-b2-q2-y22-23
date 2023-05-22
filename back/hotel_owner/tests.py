from big_b_n_b.tests_utils import BigBNBTestCase
from . import views


class TestEndpoints(BigBNBTestCase):
    def test_all_get(self):
        request = self.factory.get('/hotel_owners/')
        response = views.all_hotel_owners(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))

    def test_all_post(self):
        hotel_owner_json = self.get_new_hotel_owner_json()
        request = self.factory.post('/hotel_owners/', hotel_owner_json, format='json')
        response = views.all_hotel_owners(request)
        self.assertEqual(response.status_code, 201)

        request = self.factory.post('/hotel_owners/', hotel_owner_json, format='json')
        response = views.all_hotel_owners(request)
        self.assertEqual(response.status_code, 409)

        request = self.factory.post('/hotel_owners/', {"info": "des infos"}, fomat='json')
        response = views.all_hotel_owners(request)
        self.assertEqual(response.status_code, 400)

    def test_details_auth_get(self):
        request = self.factory.get('/hotel_owners/')
        self.add_auth_token_to_request(request, self.hotel_owner_user)
        response = views.hotel_owner_detail(request, hotel_owner_id=self.hotel_owner_obj.user_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.get_auth_hotel_owner_json())

        response = views.hotel_owner_detail(request, hotel_owner_id=-16516)
        self.assertEqual(response.status_code, 404)

    def test_details_not_auth_get(self):
        request = self.factory.get('/hotel_owners/')
        response = views.hotel_owner_detail(request, hotel_owner_id=self.hotel_owner_obj.user_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.get_not_auth_hotel_owner_json())

        response = views.hotel_owner_detail(request, hotel_owner_id=-12616)
        self.assertEqual(response.status_code, 404)

    def test_details_delete(self):
        request = self.factory.delete('/hotel_owners/')
        response = views.hotel_owner_detail(request, hotel_owner_id=self.hotel_owner_obj.user_id)
        self.assertEqual(response.status_code, 401)

        self.add_auth_token_to_request(request, self.hotel_owner_user)
        response = views.hotel_owner_detail(request, hotel_owner_id=self.hotel_owner_obj.user_id)
        self.assertEqual(response.status_code, 204)

        request = self.factory.get('/hotel_owners/')
        response = views.hotel_owner_detail(request, hotel_owner_id=self.hotel_owner_obj.user_id)
        self.assertEqual(response.status_code, 404)

