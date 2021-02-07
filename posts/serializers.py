from collections import OrderedDict
from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    date_created = serializers.ReadOnlyField()
    created_by = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
    
    def to_representation(self, value):
        repr_dict = super(CommentSerializer, self).to_representation(value)
        return OrderedDict((k, v) for k, v in repr_dict.items() 
                           if v not in [None, [], '', {}])

class PostSerializer(serializers.ModelSerializer):
    date_created = serializers.ReadOnlyField()
    created_by = UserSerializer()
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'content',
            'date_created',
            'created_by',
            'comments',
        )
    
    def to_representation(self, value):
        repr_dict = super(PostSerializer, self).to_representation(value)
        return OrderedDict((k, v) for k, v in repr_dict.items() 
                           if v not in [None, [], '', {}])