from .serializers import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.mixins import *
from rest_framework.generics import *

# API: CBV for getting all articles
class APIArticlesListView(ListModelMixin, CreateModelMixin, GenericAPIView):

    queryset = Article.objects.order_by('-article_date')
    serializer_class = ArticleSerializer

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(CreateModelMixin,self).get_serializer(*args, **kwargs)

    # using method_decorator to wrap method in function decorator
    # only registered users can retrieve articles list using api
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # only authorized users, like staff members, can create articles
    @method_decorator(staff_member_required)
    def post(self, request,  *args, **kwargs):
        kwargs['many']=True
        return self.create(request, *args, **kwargs)


# API: CBV for getting particular article & manipulating over it
class APIArticleDetailsView(RetrieveAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView):

    queryset = Article.objects.order_by('-article_date')
    serializer_class= ArticleSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(UpdateModelMixin, self).get_serializer(*args, **kwargs)

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # only authorized users, like staff members, can update articles
    @method_decorator(staff_member_required)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # only authorized users, like staff members, can delete article
    @method_decorator(staff_member_required)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
