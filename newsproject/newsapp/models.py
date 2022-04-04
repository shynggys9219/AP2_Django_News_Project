from django.db import models
from django.contrib.auth.models import AbstractUser


# Editor model to store editors in database
# Editors table in db.sqlite3
class Editor(models.Model):

    # field to store editor's name
    editor_name = models.CharField(max_length=50)

    # field to store editors's surname
    editor_surname = models.CharField(max_length=50)

    # magic method to retrieve str value of name and surname and
    # return them when the method is called
    def __str__(self) -> str:
        return " ".join((self.editor_name, self.editor_surname))


# Article model to store editors in database
# Articles table in db.sqlite3
class Article(models.Model):

    # field to store article category
    article_category = models.CharField(max_length=200)

    # field to store artcile name
    article_name = models.CharField(max_length=200)

    # field to store article's text
    article_text = models.TextField()

    # field to store article's date
    article_date = models.DateTimeField(auto_now_add=True)

    # article rating field
    article_rating = models.FloatField(default=0.0)

    # number of views of article
    article_num_of_views = models.IntegerField(default=0)

    # field to store link to editor (foreign key, M to 1 relationship)
    article_editor = models.ForeignKey(Editor, on_delete=models.CASCADE)

    # magic method to retrieve str value of article name and
    # return it when the method is called
    def __str__(self) -> str:
        return self.article_name

    # each time this article is opened
    # its number will be increased
    def increase_view_num(self):
        self.article_num_of_views += self.article_num_of_views

    def article_rate(self, newrate):
        pass


# this is extension of exising class in django.contrib.auth.models.AbstractUser
# it is slightly different from what we had before for superuser (admin)
# we have added user_avatar field to store some image
# Users table in db.sqlite3
class CustomUser(AbstractUser):

    # field to store user picture
    user_avatar = models.ImageField(upload_to="user_avatars/", default='NULL')

    # returning username when called
    def __str__(self) -> str:
        return self.username


# This model is used to store comments on articles that will be left by CustomUsers (Users)
# Comments table in db.sqlite3
class Comment(models.Model):

    # field to store comment text
    comment_text = models.TextField('comment_text')

    # field to store date of comment
    comment_date = models.DateTimeField('comment_date', auto_now_add=True)

    # field to store rating of comment
    comment_rating = models.FloatField(default=0.0)

    # field to store a link to an article
    comment_on_article = models.ForeignKey(Article, on_delete=models.CASCADE)

    # field to store a link to a user
    comment_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # returning comment text and its owner when called
    def __str__(self) -> str:
        return " ".join((self.comment_text, self.comment_owner))

    # TO-DO
    def rate_comment(self, newrate):
        pass
