from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from celery import shared_task

from .models import Cryptocurrency


@shared_task()
def update_currency():
    """
    Обновление данных криптовалют.

    При первом запуске создает в БД запись о первых 10 криптовалютах
    согласно сайту https://coinranking.com/.
    В дальнейшем получает данные с сайта и обновляет информацию в БД.
    """

    print('Обновление БД.')
    req = Request('https://coinranking.com/')
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    rows = bs.find('tbody', class_='table__body').find_all(
        'tr', class_='table__row')[1:11]
    for row in rows:
        cryptocurrency = row.find(
            'a', class_='profile__link').get_text().strip().replace('\n', '')
        values = row.find_all('div', class_='valuta')
        price = values[0].get_text().strip().replace('\n', '')
        price = '$ ' + price[1:].strip()
        market_cap = values[1].get_text().strip().replace('\n', '')
        market_cap = '$ ' + market_cap[1:].strip()
        change = row.find(
            'div', class_='change').get_text().strip().replace('\n', '')
        data = {'cryptocurrency': cryptocurrency,
                'price': price,
                'market_cap': market_cap,
                'change': change}
        obj = Cryptocurrency.objects.filter(cryptocurrency=cryptocurrency)
        if not obj:
            Cryptocurrency.objects.create(**data)
        else:
            obj.update(**data)
