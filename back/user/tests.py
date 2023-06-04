from django.contrib.auth import get_user_model

from big_b_n_b.tests_utils import BigBNBTestCase
from client.serializers import ClientSerializer
from hotel_owner.serializers import HotelOwnerSerializer
from .serializers import UserSerializerValidator


class TestUserSerializerValidator(BigBNBTestCase):
    def test_init_client(self):
        client_json: dict = self.get_new_client_json()
        with self.assertRaises(ValueError):
            UserSerializerValidator(data=client_json, serializer_class=int)

        validator = UserSerializerValidator(data=client_json, serializer_class=ClientSerializer)
        self.assertEqual(validator.serializer_class, ClientSerializer)

    def test_init_hotel_owner(self):
        self.assertEqual(UserSerializerValidator(
            data=self.get_new_hotel_owner_json(),
            serializer_class=HotelOwnerSerializer
        ).serializer_class, HotelOwnerSerializer)

    def test_is_data_valid(self):
        self.assertTrue(UserSerializerValidator(data=self.get_new_client_json(),
                                                serializer_class=ClientSerializer).is_data_valid())
        self.assertFalse(UserSerializerValidator(data={'data': "n'importe quoi"},
                                                 serializer_class=ClientSerializer).is_data_valid())
        self.assertFalse(UserSerializerValidator(data={'info': {'data': "n'importe quoi"}},
                                                 serializer_class=ClientSerializer).is_data_valid())

    def test_create_user(self):
        client_json: dict = self.get_new_client_json()
        user = UserSerializerValidator(data=client_json, serializer_class=ClientSerializer).create_user()
        client_json = client_json['info']
        self.assertEqual(client_json['mail'], user.mail)
        self.assertEqual(client_json['name'], user.name)
        self.assertEqual(client_json['lastname'], user.lastname)

        with self.assertRaises(RuntimeError):
            UserSerializerValidator(data=client_json, serializer_class=ClientSerializer).create_user()

        with self.assertRaises(RuntimeError):
            UserSerializerValidator(data={'info': "n'importe quoi"}, serializer_class=ClientSerializer).create_user()

    def test_is_duplicated(self):
        data = self.get_new_client_json()
        data['info']['mail'] = self.client_user.mail
        self.assertTrue(UserSerializerValidator(data=data, serializer_class=ClientSerializer).is_duplicated())

        self.assertFalse(UserSerializerValidator(data=self.get_new_client_json(),
                                                 serializer_class=ClientSerializer).is_duplicated())

        with self.assertRaises(RuntimeError):
            UserSerializerValidator(data={'test': "n'import quoi"}, serializer_class=ClientSerializer).is_duplicated()

    def test_get_final_data(self):
        data = self.get_new_client_json()
        with self.assertRaises(RuntimeError):
            UserSerializerValidator(data={'info': "jrr"}, serializer_class=ClientSerializer).get_final_data()

        with self.assertRaises(RuntimeError):
            UserSerializerValidator(data=data, serializer_class=ClientSerializer).get_final_data()

        validator = UserSerializerValidator(data=data, serializer_class=ClientSerializer)
        user = validator.create_user()
        final_data = validator.get_final_data()
        data['id'] = user.id
        data['info']['id'] = user.id
        self.assertEqual(final_data, data)

    def test_get_current_response(self):
        self.assertEqual(UserSerializerValidator(
            data={'id': "nze"}, serializer_class=ClientSerializer).get_current_response().status_code, 400)

        data = self.get_new_client_json()
        self.assertEqual(UserSerializerValidator(
            data=data, serializer_class=ClientSerializer).get_current_response().status_code, 201)

        self.assertTrue(get_user_model().objects.all().filter(mail=data['info']['mail']))
        