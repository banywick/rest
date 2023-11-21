from rest_framework import serializers
from .models import Book, Author, Language, Piple


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField()
    languages = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['title', 'authors', 'languages']


# class BookSerializer(serializers.ModelSerializer):
#     authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
#     languages = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True)
#     class Meta:
#         model = Book
#         fields = '__all__'


class BooksForAuthorsSerializer(serializers.Serializer):
    title = serializers.CharField()
    languages = serializers.StringRelatedField(many=True)


class AuthorSerializer(serializers.ModelSerializer):
    aut = BooksForAuthorsSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'aut']


class LanguagesSerializer(serializers.ModelSerializer):
    aut = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Language
        fields = ['title', 'aut']


"""Операции CRUD REST С простой моделью"""


class PipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piple
        fields = ['id', 'name', 'surname', 'old', 'sex']

#######################################################
class LanguageSerializer2(serializers.Serializer):
    title = serializers.CharField(max_length=20)


class AuthorSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class BookSerializer2(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    authors = AuthorSerializer2()
    languages = LanguageSerializer2(many=True)
