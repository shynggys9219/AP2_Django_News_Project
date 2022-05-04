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
         APIArticleDetailsView.as_view(), name='api-article-detail'),

    # getting all editors list
    path('editors/all/', APIEditorsListView.as_view(),
         name='api-editors-list'),

    # getting editor details
    path('editors/editor/<int:pk>/',
         APIEditorDetailsView.as_view(), name='api-editor-details'),

    # getting all users list
    path('users/all/', APICustomUsersListView.as_view(),
         name='api-users-list'),

    # getting user details
    path('users/user/<int:pk>/',
         APICustomUserDetailsView.as_view(), name='api-user-details'),

    # getting all comments list
    path('comments/all/', APICommentsListView.as_view(),
         name='api-comments-list'),

    # getting comment details
    path('comments/comment/<int:pk>/',
         APICommentDetailsView.as_view(), name='api-comment-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
