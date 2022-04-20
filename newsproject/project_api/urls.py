from django.urls import path
from .views import *


app_name='pro_api'
urlpatterns = [
    # getting all articles list
    path('articles/all/', api_articles_list , name='api-articles-list'),

    # getting article details
    path('articles/article/<int:id>/', api_article_details , name='api-articles-list'),
]
