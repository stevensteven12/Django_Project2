from django.conf.urls import url

from . import views
from django.urls import include, path


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'blog/$', views.livelog, name='livelog'),
]
