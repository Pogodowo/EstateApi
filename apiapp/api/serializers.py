from rest_framework import serializers
from ..models import baza_ogloszen,linki_otodom,test_aktywnosci

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=baza_ogloszen
        fields = ['tytul','cena', 'powierzchnia','lokalizacja','url_link','data_wystawienia','foto','cena_za_metr','liczba_pokoi','pk']



class Link_oto_dom_Serializer(serializers.ModelSerializer):
    class Meta:
        model=linki_otodom
        fields =['tytul_linka','url_linka']

class TestAktywnosciSerializer(serializers.ModelSerializer):
    class Meta:
        model=test_aktywnosci
        fields =['aktywnosc_skryptu',"status_skryptu"]
