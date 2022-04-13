from django.contrib import admin
from newsapp.models import *

# display Editor model for manipulations in admin panel
admin.site.register(Editor)

# display Article model for manipulations in admin panel
admin.site.register(Article)

# display CustomUser model
admin.site.register(CustomUser)

# display Comment model
admin.site.register(Comment)
