from rest_framework import serializers

from .models import Profile, Person, Store, Product


class PerProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price']


class PersonSerializer(serializers.ModelSerializer):
    number_person = serializers.StringRelatedField()
    product = PerProdSerializer(many=True)
    store = serializers.StringRelatedField()

    class Meta:
        model = Person
        fields = ['name', 'number_person', 'store', 'product']


class ComboProductsSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    number_person = serializers.StringRelatedField()
    store = serializers.StringRelatedField()

    class Meta:
        model = Person
        fields = ['name', 'number_person', 'store']


class ProductSerializer(serializers.ModelSerializer):
    products = ComboProductsSerializers(many=True)

    class Meta:
        model = Product
        fields = ['title', 'price', 'products']


class ComboProfileSerializer(serializers.ModelSerializer):
    store = serializers.StringRelatedField()
    product = serializers.StringRelatedField(many=True)

    class Meta:
        model = Person
        fields = ['name', 'store', 'product']


class ProfileSerializer(serializers.ModelSerializer):
    profile = ComboProfileSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['number_person', 'profile']
