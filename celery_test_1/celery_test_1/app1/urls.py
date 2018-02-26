from django.urls import path

from . import views


app_name = 'app1'
urlpatterns = [
#    path('', views.dashboard, name='dashboard'),
    path('mail', views.task_not_use_celery, name='task_not_use_celery'),
    path('', views.index, name='index'),
]