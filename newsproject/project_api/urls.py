from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'pro_api'
urlpatterns = [
    # getting all articles list
    path('articles/all/', APIArticlesListView.as_view(),
         name='api-articles-list'),

    # getting article details
    path('articles/article/<int:pk>/',
         APIArticleDetailsView.as_view(), name='api-articles-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
