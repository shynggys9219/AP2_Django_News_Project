from .views import *

# set of views generated from CBVs
# Article related views
articles_list = APIArticlesViewSet.as_view({'get': 'list', 'post': 'create'})
article_details = APIArticlesViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})


# Editor related views
editors_list = APIEditorsViewSet.as_view({'get': 'list', 'post': 'create'})
editor_details = APIEditorsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

# CustomUser related views
users_list = APICustomUsersViewSet.as_view({'get': 'list', 'post': 'create'})
user_details = APICustomUsersViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

# Comment related views
comments_list = APICommentsViewSet.as_view({'get': 'list', 'post': 'create'})
comment_details = APICommentsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
