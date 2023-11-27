from rest_framework import serializers

from .models import Profile


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    price = serializers.IntegerField()


class StoreSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)


class ProfileSerializer(serializers.Serializer):
    number_person = serializers.CharField(max_length=50)
    class Meta:
        model = Profile
        depth = 2



class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    number_person = ProfileSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    store = StoreSerializer(read_only=True)
