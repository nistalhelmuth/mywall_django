from collections import OrderedDict

from rest_framework import serializers

from .models import User
 
 
class UserSerializer(serializers.ModelSerializer):
    date_created = serializers.ReadOnlyField()
 
    class Meta(object):
        model = User
        fields = (
            'id',
            'email',
            'name',
            'city',
            'genre',
            'date_created',
            'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def to_representation(self, value):
        repr_dict = super(UserSerializer, self).to_representation(value)
        return OrderedDict((k, v) for k, v in repr_dict.items() 
                           if v not in [None, [], '', {}])

class UserDetailSerializer(serializers.ModelSerializer):
    date_created = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = (
            'id',
            'email',
            'name',
            'city',
            'visitors',
            'genre',
            'feeling',
            'date_created',
        )
    
    def to_representation(self, value):
        repr_dict = super(UserDetailSerializer, self).to_representation(value)
        return OrderedDict((k, v) for k, v in repr_dict.items() 
                           if v not in [None, [], '', {}])
