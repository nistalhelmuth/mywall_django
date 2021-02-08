from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewSet
 
urlpatterns = [
    path('general/', PostViewSet.as_view())
    #url(r'^specific/$', PostViewSet),
]

urlpatterns = format_suffix_patterns(urlpatterns)