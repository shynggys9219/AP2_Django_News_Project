from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.


def index(request):
    articles = Article.objects.order_by('-article_date')

    return render(request, 'newsapp/index.html', {"latest_articles": articles})


def get_article_by_id(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'newsapp/article.html', {"article": article})


def search_article_by_text(request, text):
    articles = list(Article.objects.filter(
        article_text__contains=text).values_list())
    print(articles)
    try:
        result = ""
        for art in articles:
            print("Here")
            result += f"<h3># {articles.index(art)}: {art[1]}</h3><br>"
        return HttpResponse(f"Search Results: <br> {result}")
    except:
        return HttpResponse(f"No such articles with text: {text}")


def archive(request):
    try:
        articles = Article.objects.all()
        result = ""
        for art in articles:
            result += f"<h3># {art.id}: {art.article_text}</h3><br>"
        return HttpResponse(f"Search Results: <br> {result}")
    except:
        return HttpResponse(f"No such articles has been added yet")
