from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']
        depth = 1
        
    # super_type = serializers.IntegerField(write_only=True) 
    #^^^^^^^ when this is active my GET in postman shows all data in the entrys EXCEPT the super_type FK data
    # when it's not I can't create a new entry because the "super_type_id" field is missing. 