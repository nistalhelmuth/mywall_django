from django.conf.urls import url
from .views import PostViewSet
 
urlpatterns = [
    url(r'^general/$', PostViewSet.as_view())
    #url(r'^specific/$', PostViewSet),
]