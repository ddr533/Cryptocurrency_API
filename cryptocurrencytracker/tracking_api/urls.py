from django.urls import path
from tracking_api.views import ListCryptocurrencyView


app_name = 'tracking_api'

urlpatterns = [
    path('v1/', ListCryptocurrencyView.as_view(), name='crypto_api')
]
