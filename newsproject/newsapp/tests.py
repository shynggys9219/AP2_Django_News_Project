from audioop import reverse
from django.test import TestCase, Client # Client is used to imitate client requests
from .models import *
from django.urls import reverse 
# Create your tests here.

class EditorModelTests(TestCase):

    def test_get_name(self):
        editor = Editor(editor_name='John', editor_surname='Legend')
        self.assertTrue(editor.get_name()=="John", "get_name() method testing failed")

    def test_get_surname(self):
        editor = Editor(editor_name="John", editor_surname="Legend")
        self.assertTrue(editor.get_surname()=="Legend", "get_surname() method testing failed")

class ArticleModelTests(TestCase):
    client = Client()
    def setUp(self):
        Editor.objects.create(id=999, editor_name="John", editor_surname="Legend")
        ed1 = Editor.objects.get(id=999)
        Article.objects.create(id=10001,
                                article_category="tech",
                                article_name="Test article name",
                                article_text="Test article text",
                                article_editor=ed1,
                                )

    def test_article_rating_increase(self):
        art = Article.objects.get(pk=10001)
        art.article_rate(5.0)
        self.assertTrue(art.article_rating==5, "New article rate is not 0.0 by default ")


    def test_article_num_of_view_increase(self):
        art = Article.objects.get(pk=10001)
        art.increase_view_num()
        self.assertEqual(art.article_num_of_views, 1, "Setting new value failed")   

class ArticleIndexViewTests(TestCase):
    client = Client()
    def setUp(self):
        Editor.objects.create(editor_name="John", editor_surname="Legend")
        ed1 = Editor.objects.get(editor_name="John")
        Article.objects.create(id=10001,
                                article_category="tech",
                                article_name="Test article name",
                                article_text="Test article text",
                                article_editor=ed1,
                                )

    def test_index_view_status(self):
        response = self.client.get(reverse('newsapp:index')) # GET / HTTP/1.1
        self.assertEqual(response.status_code, 200) # 200 -> OK

    def test_index_view_latest_articles_context(self):
        article = Article.objects.order_by('-article_date').get(pk=10001)
        response = self.client.get(reverse('newsapp:index'))
        self.assertQuerysetEqual(response.context['latest_articles'], [repr(article)])    


class ArticleGetArtByIdViewTests(TestCase):
    client = Client()
    def setUp(self):
        Editor.objects.create(editor_name="John", editor_surname="Legend")
        ed1 = Editor.objects.get(editor_name="John")
        Article.objects.create(id=10001,
                                article_category="tech",
                                article_name="Test article name",
                                article_text="Test article text",
                                article_editor=ed1,
                                )

    def test_GetArtByIdView_status(self):
        article = Article.objects.get(id=10001)
        url = reverse("newsapp:get_article_by_id", args=(article.id,))
        response = self.client.get(url) #articles/article/10001
        self.assertEqual(response.status_code, 200, "url get_article_by_id status code test failed")

    def test_ArtArchiveView_context(self):
        article = Article.objects.order_by('article_date').get(pk=10001)
        url = reverse("newsapp:archive")
        response = self.client.get(url)
        self.assertQuerysetEqual(response.context['archive_articles'], [repr(article)])