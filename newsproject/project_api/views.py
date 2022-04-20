from os import stat
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .serializers import *
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

# CSRF a mechanism of guarding against a particular type of attack, 
# which can occur when a user has not logged out of a web site, 
# and continues to have a valid session
@csrf_exempt 
def api_articles_list(request):
    """
    GETTING ALL ARTICLES ORDERED BY DATE
    """
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201) # 201 is http status code for Created
        return JsonResponse(serializer.errors, status=400) # 400 is http status code for Bad Request

@csrf_exempt
def api_article_details(request, id):

    art = get_object_or_404(Article, pk=id)
    if request.method=='GET':
        serializer = ArticleSerializer(art)
        return JsonResponse(serializer.data)
    
    elif request.method=='PUT':
        data = JSONParser().parse(request)
        print(request)
        print(art)
        serializer = ArticleSerializer(art, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method=='DELETE':
        print(art)
        art.delete()
        return HttpResponse(status=204) # 204 is http status for No Content (deleted)

