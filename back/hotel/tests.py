import json
import unittest
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Hotel
import requests

class HotelFilterTestCase(unittest.TestCase):
	
	def test_filter_bad(self):
		response = requests.get('http://192.168.1.16:8000/bad_endpoint/?min_price={price_min}&max_price={price_max}&min_rating={rating_min}&max_rating={rating_max}')
		self.assertEqual(response.status_code, 404)

	def test_filter_basic(self):
		price_min = 0
		price_max = 10000
		rating_min = 0
		rating_max = 5

		response = requests.get(f'http://192.168.1.16:8000/filter_hotels/?min_price={price_min}&max_price={price_max}&min_rating={rating_min}&max_rating={rating_max}')
		content_type = response.headers.get('Content-Type')
		self.assertEqual(content_type, 'application/json')
		data = response.json()
		self.assertIsInstance(data, list)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(data), 20)
		for hotel in data:
			self.assertGreaterEqual(hotel["price"], 0) and self.assertLessEqual(hotel["price"], 10000)
			self.assertGreaterEqual(hotel["rating"], 0) and self.assertLessEqual(hotel["rating"], 5)
			self.assertNotIn('key', hotel)
			self.assertIn('id', hotel)
			self.assertIn('hotel_owner', hotel)
			self.assertIn('name', hotel)
			self.assertIn('image', hotel)
			self.assertIn('description', hotel)
			self.assertIn('city', hotel)
			self.assertIn('rooms', hotel)
			self.assertIn('price', hotel)
			self.assertIn('rating', hotel)

	def test_filter_string(self):
		price_min = -5
		price_max = 10000
		rating_min = 0
		rating_max = 'yop'
		response = requests.get(f'http://192.168.1.16:8000/filter_hotels/?min_price={price_min}&max_price={price_max}&min_rating={rating_min}&max_rating={rating_max}')
		self.assertEqual(response.status_code, 500)

	def test_filter_neg(self):
		price_min = 0
		price_max = 10000
		rating_min = 0
		rating_max = -1
		response = requests.get(f'http://192.168.1.16:8000/filter_hotels/?min_price={price_min}&max_price={price_max}&min_rating={rating_min}&max_rating={rating_max}')
		self.assertEqual(response.status_code, 200)
		data = response.json()
		self.assertEqual(len(data), 0)
	
	def test_filter_basic_one(self):
		price_min = 50
		price_max = 100
		rating_min = 2
		rating_max = 3

		response = requests.get(f'http://192.168.1.16:8000/filter_hotels/?min_price={price_min}&max_price={price_max}&min_rating={rating_min}&max_rating={rating_max}')
		content_type = response.headers.get('Content-Type')
		self.assertEqual(content_type, 'application/json')
		data = response.json()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(data), 1)
		for hotel in data:
			self.assertGreaterEqual(hotel['price'], 50) and self.assertGreaterEqual(hotel['price'], 100)
			self.assertGreaterEqual(hotel['rating'], 2) and self.assertLessEqual(hotel['rating'], 3)


if __name__ == '__main__':
	unittest.main()
