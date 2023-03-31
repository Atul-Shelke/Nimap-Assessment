from rest_framework import serializers
from .models import client
from user.serializers import registerSerializer
class clientSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=client
        fields='__all__'
        
        
    

    def update(self, instance, validated_data):
        instance.client_name=validated_data.get('client_name',instance.client_name)
        
        instance.save()
        return instance
    
class clientSerializer1(serializers.ModelSerializer):
    created_by=serializers.StringRelatedField()
    
    class Meta:
        model=client
        fields='__all__'
        
        def to_representation(self, instance):
            rep=super(clientSerializer,self).to_representation(instance)
            rep['created_by']=instance.created_by.username
            return rep
    