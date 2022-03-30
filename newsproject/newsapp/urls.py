from django.urls import path
from .views import *

# app name to use in pairs with urls in templates
app_name = 'newsapp'

# url patterns that gives us resources when requested
# structure is path(string_url, view_name, name=url_name)
urlpatterns = [
    # index (main) page
    path('', index, name='index'),

    # getting specific article by this url
    path('articles/article/<int:id>', get_article_by_id, name='get_article_by_id'),

    # searching specific word or pattern of text in article_text column
    path('articles/search/<str:text>', search_article_by_text,
         name='search_article_by_text'),

    # getting all articles in ASC order by date
    path('articles/archive/', archive, name='archive'),
]
