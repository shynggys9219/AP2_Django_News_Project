from datetime import datetime
from django.db import models


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

    # field to store artcile name
    article_name = models.CharField(max_length=200)

    # field to store article's text
    article_text = models.TextField()

    # field to store article's date
    article_date = models.DateTimeField(default=datetime.now())

    # field to store link to editor (foreign key, M to 1 relationship)
    article_editor = models.ForeignKey(Editor, on_delete=models.CASCADE)

    # magic method to retrieve str value of article name and
    # return it when the method is called
    def __str__(self) -> str:
        return self.article_name
