from rest_framework import serializers
from .models import SuperType

class SuperTypeSerializer:
    class Meta:
        model = SuperType
        fields = ['type']