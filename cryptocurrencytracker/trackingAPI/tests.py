from django.test import TestCase

from .models import Cryptocurrency
from .worker_func import update_currency


class CryptocurrencyUpdateTestCase(TestCase):
    """Проверка работы парсера. Первоначальные данные обновляются."""

    def test_update_cryptocurrency(self):
        update_currency()
        obj = Cryptocurrency.objects.first()
        self.assertIsNotNone(obj)
        self.assertNotEqual(obj.price, '$ 0.00')
        self.assertNotEqual(obj.market_cap, '$ 0.00')
        self.assertNotEqual(obj.change, '0.00%')
