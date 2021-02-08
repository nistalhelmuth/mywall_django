from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from .models import Post, Comment
from .serializers import PostSerializer


class PostViewSet(ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        created_by = self.request.query_params.get('created_by', None)
        if created_by not in [None, '']:
            queryset = queryset.filter(created_by_id=created_by)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)