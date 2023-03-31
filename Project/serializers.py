from rest_framework import serializers
from .models import project
from user.serializers import registerSerializer
class projectserializer(serializers.ModelSerializer):
    class Meta:
        model=project
        fields='__all__'

class projectserializer1(serializers.ModelSerializer):
    created_by=serializers.StringRelatedField()
    client=serializers.StringRelatedField()
    users=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=project
        fields='__all__'

        def to_representation(self, instance):
            rep=super(registerSerializer,self).to_representation(instance)
            rep['created_by']=instance.created_by.username
            rep['client']=instance.client.client_name
            rep['users']=instance.users.username
            print(rep['users'])
            return rep