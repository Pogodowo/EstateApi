from rest_framework import serializers
from ..models import baza_ogloszen

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=baza_ogloszen
        fields = ['tytul','cena', 'powierzchnia','lokalizacja','url_link','data_wystawienia','data_zakonczenia','foto','cena_za_metr','liczba_pokoi']

