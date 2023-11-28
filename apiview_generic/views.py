from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Clock
from .serializers import ClockSerializer


@api_view(['GET'])
def my_api(request):
    clock = Clock.objects.all()

    serializer = ClockSerializer(clock, many=True)
    return Response(serializer.data)



