from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
    url(r'^posts/', include(('posts.urls', 'posts'), namespace='posts'))
]
