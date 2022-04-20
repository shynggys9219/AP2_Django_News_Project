from os import stat
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


# Create your views here.

@api_view(['GET', 'POST'])
@login_required(login_url='/login/')
def api_articles_list(request, format=None):
    """
    GETTING ALL ARTICLES ORDERED BY DATE
    """
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 201 is http status code for Created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 400 is http status code for Bad Request

@api_view(['GET', 'PUT', 'DELETE'])
@login_required(login_url='/login/')
def api_article_details(request, id, format=None):

    art = get_object_or_404(Article, pk=id)
    if request.method=='GET':
        serializer = ArticleSerializer(art)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = ArticleSerializer(art, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # 204 is http status for No Content (deleted)

