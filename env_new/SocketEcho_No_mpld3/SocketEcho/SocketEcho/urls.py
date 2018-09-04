"""SocketEcho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import echo_example.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^blog/', echo_example.views.livelog, name='echo'),
    url(r'^', echo_example.views.livelog, name='echo'),
    url(r'^download', echo_example.views.download_data, name='download_data'),
    url(r'^upload', echo_example.views.upload_data, name='upload_data'),
    url(r'^file_download', echo_example.views.file_download, name='file_download'),

]

urlpatterns += staticfiles_urlpatterns()