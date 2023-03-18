from django.db import models

class baza_ogloszen(models.Model):
    tytul = models.CharField(max_length=80,null=True,blank=True)
    lokalizacja = models.CharField(max_length=80,null=True,blank=True)
    cena = models.CharField(max_length=30,null=True,blank=True)
    cena_za_metr = models.CharField(max_length=30,null=True,blank=True)
    liczba_pokoi = models.CharField(max_length=30,null=True,blank=True)
    powierzchnia = models.CharField(max_length=20,null=True,blank=True)
    url_link = models.TextField(max_length=200,null=True,blank=True)
    foto = models.TextField(max_length=200, null=True, blank=True)
    data_wystawienia = models.DateTimeField(null=True,blank=True)
    data_zakonczenia = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.tytul

class linki_otodom(models.Model):
    tytul_linka = models.CharField(max_length=80, null=True, blank=True)
    url_linka = models.TextField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.tytul_linka

class test_aktywnosci(models.Model):
    status_skryptu= models.CharField(max_length=20,null=True,blank=True)
    aktywnosc_skryptu = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.aktywnosc_skryptu

