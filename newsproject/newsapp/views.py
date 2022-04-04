from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import *
from django.views.generic.edit import CreateView
from .forms import *

# Create your views here.


def index(request):
    articles = Article.objects.order_by('-article_date')
    cats = Article.objects.values("article_category").distinct()
    return render(request, 'newsapp/index.html', {"latest_articles": articles, "categories": cats})


def get_article_by_id(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'newsapp/article.html', {"article": article})


def search_article_by_text(request):
    try:
        if request.method=="POST":
            article_text = request.POST.get("search_field")
            print(article_text)
            if len(article_text)>0:
                search_res = Article.objects.filter(article_text__contains=article_text)
                print(search_res)
            return render(request, "newsapp/search.html",
                        {"search_res":search_res,"empty_res":search_res})
    except:
        print("SOMETHING WENT WRONG")
        return render(request, "newsapp/search.html",{"empty_res":search_res})


def archive(request):
    articles = Article.objects.all()[:100] # 2235
    return render(request, 'newsapp/archive.html', {"archive_articles": articles})

def contacts(request):
    return render(request, 'newsapp/contacts.html')

class registerView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('newsapp:index')
    template_name = 'newsapp/registration.html'