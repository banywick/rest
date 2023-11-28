from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import Person, Profile, Store, Product
from .serializers import PersonSerializer, ProfileSerializer


class PersonAPI(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ProfileAPI(ListAPIView):
    queryset = Profile.objects.select_related('persons')
    serializer_class = ProfileSerializer


class StoreAPI(ListAPIView):
    queryset = Store.objects.select_related('stors')
    serializer_class = ProfileSerializer


class ProfileAPI(ListAPIView):
    queryset = Product.objects.select_related('products')
    serializer_class = ProfileSerializer

