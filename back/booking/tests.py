from big_b_n_b.tests_utils import BigBNBTestCase
from . import views


class TestEndpoints(BigBNBTestCase):
    def test_all_get(self):
        request = self.factory.get('/bookings/')
        response = views.all_bookings(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))

    def test_all_post(self):
        request = self.factory.post('/bookings/', self.get_new_booking_json_post(), format='json')
        response = views.all_bookings(request)
        self.assertEqual(response.status_code, 201)

    def test_details_get(self):
        request = self.factory.get('/bookings/')
        response = views.bookings_details(request, booking_id=self.booking.booking_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.get_booking_json())

        response = views.bookings_details(request, booking_id=-1613216)
        self.assertEqual(response.status_code, 404)

    def test_details_delete(self):
        request = self.factory.delete('/bookings/')
        response = views.bookings_details(request, booking_id=self.booking.booking_id)
        self.assertEqual(response.status_code, 204)

        request = self.factory.get('/bookings/')
        response = views.bookings_details(request, booking_id=self.booking.booking_id)
        self.assertEqual(response.status_code, 404)

    def test_set_read(self):
        request = self.factory.patch('/set_booking_read/', {'unread': False}, format='json')
        response = views.set_read(request, booking_id=self.booking.booking_id)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/bookings/')
        response = views.bookings_details(request, booking_id=self.booking.booking_id)
        self.assertFalse(response.data['unread'])

        request = self.factory.patch('/set_booking_read/', {'nbfrifr': False}, format='json')
        response = views.set_read(request, booking_id=self.booking.booking_id)
        self.assertEqual(response.status_code, 400)

        request = self.factory.patch('/set_booking_read/', {'unread': 'not true'}, format='json')
        response = views.set_read(request, booking_id=self.booking.booking_id)
        self.assertEqual(response.status_code, 400)

    def test_set_approved(self):
        request = self.factory.patch('/set_booking_approved/', {'approved': True}, format='json')
        response = views.set_approved(request, booking_id=self.booking.booking_id)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/bookings/')
        response = views.bookings_details(request, booking_id=self.booking.booking_id)
        self.assertTrue(response.data['approved'])

        request = self.factory.patch('/set_booking_approved/', {'fefz': True}, format='json')
        response = views.set_approved(request, booking_id=self.booking.booking_id)
        self.assertEqual(response.status_code, 400)

        request = self.factory.patch('/set_booking_approved/', {'approved': 'not true'}, format='json')
        response = views.set_approved(request, booking_id=self.booking.booking_id)
        self.assertEqual(response.status_code, 400)

