from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import status, views
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# API: CBV for getting all articles
class APIArticlesListView(views.APIView):

    # using method_decorator to wrap method in function decorator
    # only registered users can retrieve articles list using api
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, format=None):

        # getting articles ordered by date in DESC order
        articles = Article.objects.order_by('-article_date')

        # serialization of queryset to be 'dict'
        serializer = ArticleSerializer(articles, many=True)

        # returning json like response
        return Response(serializer.data)

    # only authorized users, like staff members, can create articles
    @method_decorator(staff_member_required)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API: CBV for getting particular article & manipulating over it
class APIArticleDetailsView(views.APIView):

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, pk, format=None):
        serializer = ArticleSerializer(get_object_or_404(Article, pk=pk))
        return Response(serializer.data)

    # only authorized users, like staff members, can update articles
    @method_decorator(staff_member_required)
    def put(self, request, pk, format=None):

        # using get_object_or_404 shortcut to get article or to get PNF(404)error
        # partial=True means you can update part of an article,
        # skipping unnecessary updates/data providing
        serializer = ArticleSerializer(get_object_or_404(Article, pk=pk),
                                       data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # only authorized users, like staff members, can delete article
    @method_decorator(staff_member_required)
    def delete(self, request, pk, format=None):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
