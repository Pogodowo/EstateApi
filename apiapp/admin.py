from django.contrib import admin


from .models import baza_ogloszen,linki_otodom,test_aktywnosci

admin.site.register(baza_ogloszen)
admin.site.register(linki_otodom)
admin.site.register(test_aktywnosci)