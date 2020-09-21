from django.contrib import admin
from .models import UserAuthor , Article
# Register your models here.

admin.site.register(UserAuthor)
admin.site.register(Article)