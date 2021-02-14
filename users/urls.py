from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserProfileAPIView, authenticate_user, register_user

urlpatterns = [
    path('register/', register_user),
    path('login/', authenticate_user),
    path('profile/<int:pk>/', UserProfileAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
