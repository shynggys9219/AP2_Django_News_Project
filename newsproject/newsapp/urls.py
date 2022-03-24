from django.urls import path
from .views import *

app_name = 'newsapp'
urlpatterns = [
    path('', index, name='index'),
    path('articles/article/<int:id>', get_article_by_id, name='get_article_by_id'),
    path('articles/search/<str:text>', search_article_by_text, name='search_article_by_text'),
    path('articles/archive/', archive, name='archive'),
]
