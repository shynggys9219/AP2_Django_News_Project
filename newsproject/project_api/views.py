from .serializers import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.mixins import *
from rest_framework.generics import *
from rest_framework import permissions # new import
from .permissions import IsStaffOrNot

# API: CBV for getting all articles
class APIArticlesListView(ListCreateAPIView):

    queryset = Article.objects.order_by('-article_date')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(ListCreateAPIView,self).get_serializer(*args, **kwargs)


# API: CBV for getting particular article & manipulating over it
# there are other options: 
#      RetrieveDestroy-, RetrieveUpdate-, Retrieve-, Update-, DestroyAPIView
class APIArticleDetailsView(RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.order_by('-article_date')
    serializer_class= ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)

# API: CBV for getting all editors
class APIEditorsListView(ListCreateAPIView):

    queryset = Editor.objects.all()
    serializer_class = EditorSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(ListCreateAPIView,self).get_serializer(*args, **kwargs)


# API: CBV for getting particular editor & manipulating over it
# there are other options: 
#      RetrieveDestroy-, RetrieveUpdate-, Retrieve-, Update-, DestroyAPIView
class APIEditorDetailsView(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class= EditorSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)

# API: CBV for getting all comments
class APICommentsListView(ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(ListCreateAPIView,self).get_serializer(*args, **kwargs)


# API: CBV for getting particular comment & manipulating over it
# there are other options: 
#      RetrieveDestroy-, RetrieveUpdate-, Retrieve-, Update-, DestroyAPIView
class APICommentDetailsView(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class= CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)

# API: CBV for getting all users
class APICustomUsersListView(ListCreateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(ListCreateAPIView,self).get_serializer(*args, **kwargs)


# API: CBV for getting particular user & manipulating over it
# there are other options: 
#      RetrieveDestroy-, RetrieveUpdate-, Retrieve-, Update-, DestroyAPIView
class APICustomUserDetailsView(RetrieveUpdateDestroyAPIView):

    queryset = CustomUser.objects.all()
    serializer_class= CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)
