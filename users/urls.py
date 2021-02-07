from django.conf.urls import url
from .views import register_user, authenticate_user, UserProfileAPIView
 
urlpatterns = [
    url(r'^register/$', register_user),
    url(r'^login/$', authenticate_user),
    url(r'^profile/$', UserProfileAPIView.as_view())
]