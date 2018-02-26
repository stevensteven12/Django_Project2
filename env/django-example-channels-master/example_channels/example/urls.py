from django.conf.urls import url
from example.views import log_in, log_out, sign_up, user_list, index_test

app_name='example'
urlpatterns = [
    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^log_out/$', log_out, name='log_out'),
    url(r'^sign_up/$', sign_up, name='sign_up'),
    url(r'^$', user_list, name='user_list'),

    url(r'^index_test/$', index_test, name='index_test'),
]
