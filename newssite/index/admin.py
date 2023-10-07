from django.contrib import admin
from .models import *

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(News, NewsAdmin)

