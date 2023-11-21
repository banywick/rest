from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author, Language, Piple
from .serializers import AuthorSerializer, LanguagesSerializer, PipleSerializer, BookSerializer


# class BookAPIView(APIView):
#     serializer_class = BookSerializer
#
#     def post(self, request):
#         input_value = request.data['title']
#         books = Book.objects.filter(title=input_value)
#         return Response({'books': BookSerializer(books, many=True).data})


class BookAPIView(APIView):

    def post(self, request):
        print(request.data)
        serializer = BookSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)



class ViewBook(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)









class AuthorAPIView(APIView):
    serializer_class = AuthorSerializer

    def post(self, request):
        # input_value = request.data['title']

        query = Author.objects.prefetch_related()
        return Response({'authors': AuthorSerializer(query, many=True).data})


class LanguageAPIView(APIView):
    serializer_class = LanguagesSerializer

    def post(self, request):
        # input_value = request.data['title']

        query = Language.objects.all()
        return Response({'language': LanguagesSerializer(query, many=True).data})


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

