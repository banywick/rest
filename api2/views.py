from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import Person, Profile, Store, Product
from .serializers import ProductSerializer, PersonSerializer, ProfileSerializer


class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StoreAPI(ListAPIView):
    queryset = Store.objects.prefetch_related('products')
    serializer_class = {}


class ProfileAPI(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PersonAPI(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
