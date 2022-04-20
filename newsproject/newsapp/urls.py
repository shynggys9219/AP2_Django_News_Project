from django.urls import path
from .views import *
from django.contrib.auth.views import auth_login

# app name to use in pairs with urls in templates
app_name = 'newsapp'

# url patterns that gives us resources when requested
# structure is path(string_url, view_name, name=url_name)
urlpatterns = [
    # index (main) page
    path('', IndexView.as_view(), name='index'),

    # getting specific article by this url
    path('articles/article/<int:pk>/', ArticleDetailView.as_view(), name='get_article_by_id'),

    # searching specific word or pattern of text Article table
    path('articles/search/', SearchView.as_view(), name='search_article_by_text'),

    #if search is successful, we redirect the user to the next page
    path('articles/search/<str:text>', SearchSuccessView.as_view(), name='search_success'),

    # getting all articles in ASC order by date
    path('articles/archive/', ArchiveView.as_view(), name='archive'),

    # contacts page url
    path('contacts/', ContactsView.as_view(), name='contacts'),

    # profile page url
    path('profile/', ProfileView.as_view(), name='profile'),

    # profile changing page url
    path('profile/change/', ProfileChangeView.as_view(), name='profile_change'),

    # leave commentary 
    path('articles/article/leavecomment/', LeaveCommentView.as_view(), name='leave_comment'),

    # like commentary 
    path('articles/article/like/', CommentLikeView.as_view(), name='like_comment'),

    # like article
    path('articles/article/like_article/', ArticleDetailView.as_view(), name='like_article'),


    # AUTH PART
    # localhost:8000/login
    path('', auth_login, name="login"),

    # localhost:8000/register
    path("register/", registerView.as_view(), name="registration"),
]
