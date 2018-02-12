from django.conf.urls import url
from django.contrib import admin
from blog.views import index, remove

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$', index, name='index'),
    url(r'^blog/remove/(?P<article_id>\d+)/$', remove, name='remove'),
]

