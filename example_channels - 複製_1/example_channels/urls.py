from django.conf.urls import include, url
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('example/', include('example.urls')),
#    url(r'^', include('example.urls', namespace='example')),

    path('admin/', admin.site.urls),
]
