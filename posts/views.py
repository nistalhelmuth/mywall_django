from django.http import Http404
from django.shortcuts import render
from mywall.pagination import CustomPagination
from rest_framework import status, viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from users.models import User

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(ListCreateAPIView):
    queryset = Post.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        created_by = self.request.query_params.get('created_by', None)
        if created_by not in [None, '']:
            queryset = queryset.filter(created_by_id=created_by)
        return queryset

    def post(self, request, format=None):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CommentViewSet(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Comment.objects.filter(post__id = pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comments = self.get_object(pk)
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            try:
                serializer.save(created_by = request.user)
                Post.objects.get(id = pk).comments.add(serializer.data["id"])
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            except Post.DoesNotExist:
                comment = Comment.objects.get(id=serializer.data["id"])
                comment.delete()
                raise Http404
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
