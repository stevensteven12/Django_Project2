from django.conf.urls import url
from example.views import log_in, log_out, user_list
from django.urls import include, path
from . import views

app_name = 'example'
urlpatterns = [
 #   path('', views.index, name='index'),
 #   path('example/', include('example.urls')),
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('', views.user_list, name='user_list'),
    path('sign_up', views.sign_up, name='sign_up'),

]
