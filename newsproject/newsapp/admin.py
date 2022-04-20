from django.contrib import admin
from newsapp.models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ('article_name','article_text', 'article_editor')
    list_display = ('article_name', 'article_editor')
    list_filter = ['article_rating', 'article_editor']
    search_fields = ['article_text', 'article_name']

class CustomUserAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'is_staff', 'is_active')


# display Editor model for manipulations in admin panel
admin.site.register(Editor)

# display Article model for manipulations in admin panel
admin.site.register(Article, ArticleAdmin)

# display CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)

# display Comment model
admin.site.register(Comment)
