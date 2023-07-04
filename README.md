# Cryptocurrency_API
#### Описание
Приложение получает данные о курсах криптовалют, сохраняет их в базе и имеет API для доступа к ним 

#### Технологии
* Python 3.10
* Django 3.2
* Django rest_framework 3.12
* Sqlite3
* beautifulsoup4  4.12.2
* Celery 5.3.1
#### Как запустить проект:
* Клонировать репозиторий и перейти в него в командной строке:
    * git@github.com:ddr533/Cryptocurrency_API.git
    * cd cryptocurrencytracker


* Cоздать и активировать виртуальное окружение:
  * если у вас Windows: python -m venv env
  * если у вас Linux/macOS: source env/bin/activate

  
* Установить зависимости из файла requirements.txt: 
  * python -m pip install --upgrade pip
  * pip install -r requirements.txt

  
* Выполнить миграции: 
  * python manage.py makemigrations
  * python manage.py migrate


* Установить rabbitmq


* Запустить проект:
    * celery -A cryptocurrencytracker worker -l  info
    * python manage.py runserver
