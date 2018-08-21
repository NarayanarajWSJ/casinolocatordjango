from django.shortcuts import render
from rest_framework import generics
from casino_finder.models import Casino
from casino_finder.serializer import CasinoSerializer

# Create your views here.

class ListCasino(generics.ListCreateAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer 
