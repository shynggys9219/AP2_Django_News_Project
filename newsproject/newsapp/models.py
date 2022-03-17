from datetime import datetime
from tkinter import E
from django.db import models

# Create your models here.
class Editor(models.Model):

    editor_name = models.CharField(max_length=50)
    editor_surname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return " ".join((self.editor_name, self.editor_surname))

class Article(models.Model):

    article_name = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField(default=datetime.now())
    article_editor = models.ForeignKey(Editor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.article_name