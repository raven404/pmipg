from django.contrib import admin
from .models import Category, News, NewsView, video
# Register your models here.


class NewsD(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'author')
    list_per_page = 10


class videoD(admin.ModelAdmin):
    list_display = ('title', 'timestamp',)
    list_per_page = 10


admin.site.register(Category)
# admin.site.register(NewsView)
admin.site.register(News, NewsD)
admin.site.register(video, videoD)
