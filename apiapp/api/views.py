from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import  PostModelSerializer
from ..models import baza_ogloszen
from django.utils import timezone
import datetime
import sys

@api_view(['GET','POST'])
def ogl_list(request):
    if request.method == 'GET':
        qs = baza_ogloszen.objects.all()
        serializer = PostModelSerializer(qs,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostModelSerializer(data = request.data)
        print('coś działa')
        sys.stdout.flush()
        baza_ogloszen.objects.create(tytul=request.data['tytul'], url_link=request.data['url_link'],
                                     lokalizacja=request.data['lokalizacja'], powierzchnia=request.data['powierzchnia'],
                                     cena=request.data['cena'], cena_za_metr=request.data['cena_za_metr'],
                                     liczba_pokoi=request.data['liczba_pokoi'],
                                     data_wystawienia=datetime.datetime.now(tz=timezone.utc),
                                     data_zakonczenia=None)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)