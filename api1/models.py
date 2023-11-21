from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ForeignKey('Author', on_delete=models.PROTECT, related_name='aut')
    languages = models.ManyToManyField('Language', related_name='lan')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Language(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


"""Операции CRUD REST С простой моделью"""


class Piple(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    old = models.IntegerField()
    sex = models.CharField(max_length=1, default='m')
