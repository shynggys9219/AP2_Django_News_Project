from rest_framework import routers
from .viewsets import *

default_router = routers.DefaultRouter()
default_router.register(r'articles', APIArticlesViewSet)
default_router.register(r'users', APICustomUsersViewSet)
default_router.register(r'editors', APIEditorsViewSet)
default_router.register(r'comments', APICommentsViewSet)