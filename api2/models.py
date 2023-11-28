from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Store(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Profile(models.Model):
    number_person = models.CharField(max_length=50)


    def __str__(self):
        return self.number_person


class Person(models.Model):
    name = models.CharField(max_length=50)
    number_person = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True, related_name='persons')
    product = models.ManyToManyField(Product, related_name='products')
    store = models.ForeignKey('Store', on_delete=models.CASCADE, related_name='stors')

    def __str__(self):
        return self.name
