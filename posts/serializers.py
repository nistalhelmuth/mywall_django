from .models import Post, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    date_created = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    date_created = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'