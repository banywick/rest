from rest_framework import serializers
from .models import Book, Author, Language


class AuthorSerializer(serializers.ModelSerializer):

    books = serializers.CharField(source='author.title', read_only=True)
    # languages = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name','books']


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='authors.name', read_only=True)
    languages = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['title', 'author_name', 'languages']


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        # fields = ['title']
