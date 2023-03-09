

from django.urls import path
from .views import ogl_list,linki_oto

urlpatterns = [
    path('ogloszenia/', ogl_list),
    path('linki_oto/', linki_oto),
]
