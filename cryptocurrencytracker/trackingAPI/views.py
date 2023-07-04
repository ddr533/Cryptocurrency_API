from rest_framework import generics

from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer


class ListCryptocurrencyView(generics.ListAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
