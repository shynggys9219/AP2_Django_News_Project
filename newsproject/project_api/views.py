from .serializers import *
from rest_framework import response, reverse
from rest_framework.views import APIView  # used for APIRoot
from rest_framework import permissions  # used to set permissions on api access
from .permissions import IsStaffOrNot  # custom permission for accessing api
# using ModelViewSet class to include all the HTTP protocol methods in one CBV
from rest_framework import viewsets


# API Root 127.0.0.1:{Port_value_here or 8000 by default}/api
# class APIRoot(APIView):
#     permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

#     def get(self, request, format=None):
#         return response.Response({
#             'artiles-list': reverse.reverse('pro_api:api-articles-list', request=request, format=format),
#             'users-list': reverse.reverse('pro_api:api-users-list', request=request, format=format),
#             'editors-list': reverse.reverse('pro_api:api-editors-list', request=request, format=format),
#             'comments-list': reverse.reverse('pro_api:api-comments-list', request=request, format=format)
#         })


# API: CBV for getting all articles
class APIArticlesViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.order_by('-article_date')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)


# API: CBV for getting all editors
class APIEditorsViewSet(viewsets.ModelViewSet):

    queryset = Editor.objects.all()
    serializer_class = EditorSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)


# API: CBV for getting all comments
class APICommentsViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)


# API: CBV for getting all users
class APICustomUsersViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)
