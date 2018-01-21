from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('menu', views.menu, name='menu'),
    path('meta', views.meta, name='meta'),
    path('', views.welcome, name='welcome'),
    path('restaurants_list', views.restaurants_list, name='restaurants_list'),
]