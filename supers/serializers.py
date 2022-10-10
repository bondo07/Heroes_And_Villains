from rest_framework import serializers
from .models import Super

class SuperSerializer:
    class Meta:
        product = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type_id']