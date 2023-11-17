from rest_framework import serializers
from .models import Book, Author, Language


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField()
    languages = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['title', 'authors', 'languages']


class BooksForAuthorsSerializer(serializers.Serializer):
    title = serializers.CharField()
    languages = serializers.StringRelatedField(many=True)


class AuthorSerializer(serializers.ModelSerializer):
    aut = BooksForAuthorsSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'aut']


# class LangForLangSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     authors = serializers.StringRelatedField(many=True , read_only=True)


class LanguagesSerializer(serializers.ModelSerializer):
    aut = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Language
        fields = ['title', 'aut']
