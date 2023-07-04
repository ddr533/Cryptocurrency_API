from time import sleep

from .worker_func import update_currency

while True:
    update_currency()
    sleep(15)
