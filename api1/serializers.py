from rest_framework import serializers
from .models import Book


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Autor
#         fields = '__all__'
#

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='authors.name', read_only=True)
    print(author_name)

    class Meta:
        model = Book
        fields = ['title', 'author_name']
