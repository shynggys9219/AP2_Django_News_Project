from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import *
from .forms import *
from django.db.models import CharField, TextField
from django.db.models import Q


# Create your views here.
# Generic CBV for Index page
class IndexView(ListView):
    template_name = "newsapp/index.html"
    context_object_name = "latest_articles"
    queryset = Article.objects.order_by('-article_date')

    # adding additional context to already existing context above
    def get_context_data(self, **kwargs):
        # getting existing context value (latest_articles here rn)
        context = super().get_context_data(**kwargs)
        # adding popular articles
        context['popular_articles'] = Article.objects.filter(
            article_num_of_views__gt=100).order_by('-article_num_of_views')[:4]
        # adding categories
        context['categories'] = Article.objects.values(
            "article_category").distinct()
        # context['arts_by_cats'] = Article.objects.filter() # TO-DO
        return context

# Generic CBV for Article page


class ArticleDetailView(DetailView):
    model = Article
    template_name = "newsapp/article.html"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        article = Article.objects.get(pk=kwargs['object'].id)
        article.increase_view_num()
        article.save()
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = Article.objects.order_by('-article_date')
        context['popular_articles'] = Article.objects.filter(
            article_num_of_views__gt=100).order_by('-article_num_of_views')[:4]
        art_category = kwargs['object'].article_category
        context['related_articles'] = Article.objects.filter(
            article_category=art_category).order_by('-article_num_of_views')[:8]
        context['form'] = CommentForm()
        context['comments_on_article'] = Comment.objects.filter(
            comment_on_article=kwargs['object'].id)
        context['categories'] = Article.objects.values(
            "article_category").distinct()
        return context

    def post(self, request):
        if request.method == 'POST':
            article_rate = request.POST.get('article_rate')
            article = Article.objects.get(id=request.POST.get('article_id'))
            article.article_rate(float(article_rate))
            article.save()
            return redirect("newsapp:get_article_by_id",
                            pk=request.POST.get('article_id'))


# Custom class based view for searching any matching text in Article table
class SearchView(View):
    paginated_by = 5
    # overriding post method to accept request.POST and work with its content

    def post(self, request):
        try:
            if request.method == "POST" and len(request.POST.get("search_field")) > 0:
                searching_text = request.POST.get("search_field")
                return redirect("newsapp:search_success", text=searching_text)
            else:
                return render(request, "newsapp/search.html",
                              {"empty_res": "There is no article"})
        except Exception as e:
            print(e)
            return render(request, "newsapp/search.html",
                          {"empty_res": f"No articles have been found by {request.POST.get('search_field')}"})


# Custom class based view for successful search
class SearchSuccessView(View):

    # override get() method to return successful result
    # if any matching was in Article table
    def get(self, request, text):

        # getting fields that are either CharField
        # or TextField to search later in these fields
        fields = [field for field in Article._meta.fields if isinstance(
            field, CharField) or isinstance(field, TextField)]

        # list of querysets using Q class. Logic is field.name might be either
        # article_category, name or text which corresponds to the fields above
        queries = [Q(**{field.name + "__icontains": text}) for field in fields]
        # print(fields[0].name)
        qs = Q()
        for query in queries:
            # here is queryset which might be equal to next values
            # (AND: ('article_category__icontains', 'str_text_here'))
            # (OR: ('article_category__icontains', 'str_text_here'),
            #       ('article_name__icontains', 'str_text_here'))
            # (OR: ('article_category__icontains', 'str_text_here'),
            #       ('article_name__icontains', 'str_text_here'),
            #       ('article_text__icontains', 'str_text_here'))
            qs = qs | query

        # getting result filtering by qs (querysets)
        # that have been created above
        search_res = Article.objects.filter(qs)
        return render(request, "newsapp/search.html",
                      {"search_res": search_res, "empty_res": "There is no article"})


# Generic CBV for Archive of articles
class ArchiveView(ListView):
    template_name = 'newsapp/archive.html'
    context_object_name = "archive_articles"
    queryset = Article.objects.all()[:100]  # 2235
    paginate_by = 10

# Generic CBV for Contacts page


class ContactsView(TemplateView):
    template_name = "newsapp/contacts.html"

# Generic CBV for Profile page


class ProfileView(TemplateView):
    template_name = "newsapp/user_page.html"

# Generic CBV for Profile changing page


class ProfileChangeView(FormView):
    template_name = "registration/user_change_page.html"
    form_class = CustomUserChangeForm

# Generic CBV for Registration page


class registerView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'newsapp/registration.html'

# Generic CBV for leaving comments on Article


class LeaveCommentView(View):

    def post(self, request):
        if request.method == 'POST':
            comment_on_article = request.POST.get('comment_on_article')
            new_comment = Comment(comment_text=request.POST.get('comment_text'),
                                  comment_owner=CustomUser.objects.get(
                id=request.user.id),
                comment_on_article=Article.objects.get(id=comment_on_article))
            new_comment.save()
            return redirect("newsapp:get_article_by_id",
                            pk=request.POST.get('comment_on_article'))


class CommentLikeView(View):
    def post(self, request):
        if request.method == 'POST':
            comment_rate = request.POST.get('comment_rate')
            comment_obj = Comment.objects.get(
                id=request.POST.get('comment_id'))
            comment_obj.rate_comment(float(comment_rate))
            comment_obj.save()
            return redirect("newsapp:get_article_by_id",
                            pk=request.POST.get('article_id'))
