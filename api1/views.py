from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author, Language
from .serializers import BookSerializer, AuthorSerializer, LanguagesSerializer


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

        query = Author.objects.prefetch_related()
        return Response({'authors': AuthorSerializer(query, many=True).data})


class LanguageAPIView(APIView):
    serializer_class = LanguagesSerializer
    def post(self, request):
        # input_value = request.data['title']

        query = Language.objects.all()
        return Response({'language': LanguagesSerializer(query, many=True).data})






