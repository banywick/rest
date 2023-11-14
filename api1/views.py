from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer


@api_view(['POST'])
def get_page(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


def get_page2(request):
    return render(request, 'first_api.html')


class BookAPIView(APIView):
    def post(self, request):
        books = Book.objects.select_related('authors')
        for book in books:
            print(book.title, book.authors.name)
        return Response({'books': BookSerializer(books, many=True).data, '334': '45874'})

