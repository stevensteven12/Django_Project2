from django.urls import path

from . import views
"""""
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""

app_name = 'stock_api'
urlpatterns = [
    path('', views.index, name='index'),
    path('index_1', views.index_1, name='index_1'),
    path('index_2', views.index_2, name='index_2'),
    path('menu', views.menu, name='menu'),
    path('draw_line', views.draw_line, name='draw_line'),
    path('draw_line_2', views.draw_line_2, name='draw_line_2'),
    path('draw_line_3', views.draw_line_3, name='draw_line_3'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]