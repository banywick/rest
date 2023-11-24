from rest_framework import serializers
from .models import Piple




"""Операции CRUD REST С простой моделью"""


class PipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piple
        fields = ['id', 'name', 'surname', 'old', 'sex']



