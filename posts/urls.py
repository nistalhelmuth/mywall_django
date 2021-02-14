from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewSet, CommentViewSet
 
urlpatterns = [
    path('', PostViewSet.as_view(), name="posts-general"),
    path('<int:pk>/', CommentViewSet.as_view(), name="post-specific")
]

urlpatterns = format_suffix_patterns(urlpatterns)