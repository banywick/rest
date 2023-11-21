import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, DataSerializer


class BookAPIView(APIView):
    serializer_class = BookSerializer

    def post(self, request):
        input_value = request.data['title']
        books = Book.objects.filter(title=input_value)
        return Response({'books': BookSerializer(books, many=True).data})


class AuthorAPIView(APIView):
    serializer_class = AuthorSerializer

    def post(self, request):
        # input_value = request.data['title']
        query = Author.objects.all()
        return Response({'author': AuthorSerializer(query, many=True).data})


@api_view(['GET', 'POST'])
def data_create_view(request):

    data = request.data
    serializer = DataSerializer(data=data)
    if serializer.is_valid():
        print(serializer.data)
        author = Author(**serializer.validated_data)
        author.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
# else:
#     return JsonResponse({'message': 'Только POST запросы разрешены'}, status=405)
#     return JsonResponse({'name':'johan'})
