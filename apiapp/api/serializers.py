from rest_framework import serializers
from ..models import baza_ogloszen,linki_otodom

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=baza_ogloszen
        fields = ['tytul','cena', 'powierzchnia','lokalizacja','url_link','data_wystawienia','data_zakonczenia','foto','cena_za_metr','liczba_pokoi']



class Link_oto_dom_Serializer(serializers.ModelSerializer):
    class Meta:
        model=linki_otodom
        fields =['tytul_linka','url_linka']
