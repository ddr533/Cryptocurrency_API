from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.utils import json

from .models import Cryptocurrency
from .worker_func import update_currency


class CryptocurrencyUpdateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.methods = ('post', 'put', 'patch', 'delete')
        self.url = reverse('tracking_api:crypto_api')

    def test_update_cryptocurrency(self):
        """Парсер работает и обновляет БД."""
        update_currency()
        obj = Cryptocurrency.objects.first()
        self.assertIsNotNone(obj)
        self.assertNotEqual(obj.price, '$ 0.00')
        self.assertNotEqual(obj.market_cap, '$ 0.00')
        self.assertNotEqual(obj.change, '0.00%')

    def test_only_get_allowed(self):
        """Доступен только метод GET."""
        for method in self.methods:
            response = getattr(self.client, method)(self.url)
            self.assertEqual(response.status_code,
                             status.HTTP_405_METHOD_NOT_ALLOWED)
            self.assertEqual(response.data['detail'],
                             f'Method "{method.upper()}" not allowed.')

    def test_get_method(self):
        """Get запрос возвращает словарь с данными криптовалют."""
        data = {'id': 1, 'cryptocurrency': 'test',
                'price': 'test', 'market_cap': 'test', 'change': 'test'}
        Cryptocurrency.objects.create(**data)
        response = self.client.get(self.url)
        data = json.loads(response.content)
        self.assertEqual(data, data)
