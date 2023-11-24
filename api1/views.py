from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Piple
from .serializers import PipleSerializer

"""Операции CRUD REST С простой моделью"""


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/all',
        'Search by name': '/?name=name',
        'Search by sex': '/?sex=f or m',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/piple/pk/delete'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_piple(request):
    piple = PipleSerializer(data=request.data)
    if Piple.objects.filter(**request.data).exists():
        raise serializers.ValidationError('такая запись уже существует')
    if piple.is_valid():
        piple.save()
        return Response(piple.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_piple(request):
    if request.query_params:
        piple = Piple.objects.filter(**request.query_params.dict())
    else:
        piple = Piple.objects.all()

    if piple:
        serializer = PipleSerializer(piple, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_piple(request, pk):
    piple = Piple.objects.get(pk=pk)
    data = PipleSerializer(instance=piple, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_piple(request, pk):
    piple = get_object_or_404(Piple, pk=pk)
    piple.delete()
    return Response(status=status.HTTP_202_ACCEPTED)




