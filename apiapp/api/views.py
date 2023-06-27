#############################################################
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
##########################################################
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import  PostModelSerializer,Link_oto_dom_Serializer,TestAktywnosciSerializer
from ..models import baza_ogloszen,linki_otodom,test_aktywnosci
from django.utils import timezone
import datetime
import sys

@api_view(['GET','POST','PUT'])
def ogl_list(request):
    if request.method == 'GET':
        qs = baza_ogloszen.objects.all()
        serializer = PostModelSerializer(qs,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostModelSerializer(data = request.data)
        print('coś działa')
        sys.stdout.flush()
        baza_ogloszen.objects.create(tytul=request.data["tytul"], url_link=request.data["url_link"],
                                     lokalizacja=request.data["lokalizacja"], powierzchnia=request.data["powierzchnia"],
                                     cena=request.data["cena"], cena_za_metr=request.data["cena_za_metr"],
                                     liczba_pokoi=request.data["liczba_pokoi"],
                                     foto=request.data["foto"],
                                     data_wystawienia=datetime.datetime.now(tz=timezone.utc),
                                     )
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_CREATED)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#############################PUT#####################################################################################
# @api_view(['GET','PUT'])
# def update_element(request,pk):
#     try:
#         snippet = baza_ogloszen.objects.get(pk=pk)
#     except baza_ogloszen.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#         serializer = PostModelSerializer(snippet, data=request.data)
#         data.tytul=("zaktyalizowałem coć")
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return HttpResponse("nie działa")

class OglUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = baza_ogloszen.objects.all()
    serializer_class = PostModelSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

            ##

ogl_update_view = OglAPIView.as_view()

    ###################dotąd rzeźbię##############################################



#######################################################################################################################

@api_view(['GET','POST'])
def linki_oto(request):
    if request.method == 'GET':
        qs = linki_otodom.objects.all()
        serializer = Link_oto_dom_Serializer(qs,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Link_oto_dom_Serializer(data = request.data)
        print('coś działa')
        sys.stdout.flush()
        linki_otodom.objects.create(tytul_linka=request.data['tytul_linka'], url_linka=request.data['url_linka'],
                                     )
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def test_aktywnosci_view(request):
    if request.method == 'GET':
        qs = test_aktywnosci.objects.all()
        serializer = TestAktywnosciSerializer(qs,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TestAktywnosciSerializer(data = request.data)
        print('coś działa')
        sys.stdout.flush()
        test_aktywnosci.objects.create(status_skryptu=request.data['status_skryptu'],aktywnosc_skryptu=datetime.datetime.now(tz=timezone.utc)
                                     )
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)