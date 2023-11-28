from django.db import models


class Clock(models.Model):
    brand = models.CharField(max_length=50)
    price = models.IntegerField()


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    number_profile = models.CharField(max_length=100)




class Book(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    profile = models.OneToOneField('Profile', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField('Genre', related_name='genres')
