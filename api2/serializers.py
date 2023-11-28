from rest_framework import serializers

from .models import Profile, Person


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    price = serializers.IntegerField()


class StoreSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)


class PersonSerializerProfile(serializers.ModelSerializer):
    # product = serializers.StringRelatedField(many=True)
    # store = serializers.StringRelatedField()

    class Meta:
        model = Person
        # fields = ['name', 'product', 'store']
        fields = '__all__'
        depth = 1


class ProfileSerializer(serializers.ModelSerializer):
    persons = PersonSerializerProfile()

    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    number_person = ProfileSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    store = StoreSerializer(read_only=True)
