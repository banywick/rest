from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import Person, Profile
from .serializers import PersonSerializer, ProfileSerializer


class PersonAPI(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ProfileAPI(ListAPIView):
    queryset = Profile.objects.select_related('persons')
    serializer_class = ProfileSerializer
