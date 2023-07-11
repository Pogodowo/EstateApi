

from django.urls import path
from .views import ogl_list,linki_oto,test_aktywnosci_view,ogl_update_view

urlpatterns = [
    path('ogloszenia/', ogl_list),
    path('linki_oto/', linki_oto),
    path('aktywnosc/', test_aktywnosci_view),
    path('ogloszenia/<int:pk>/', ogl_update_view.as_view()),
]
