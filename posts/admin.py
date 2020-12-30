from django.contrib import admin

# Register your models here.
from .models import Author, Category, Post, Comment, PostView, Team, TeamView


class AuthorD(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    list_per_page = 10


class PostD(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'author')
    # list_filter = ('author',)
    list_per_page = 10
    # search_fields = ('title',)

    # def get_ordering(self, request):
    #     if request.user.is_superuser:
    #         return('title', '-timestamp')
    #     return('title',)


class TeamD(admin.ModelAdmin):
    list_display = ('name', 'timestamp', 'author')
    list_per_page = 10


admin.site.register(Author, AuthorD)
admin.site.register(Category)
admin.site.register(Post, PostD)
admin.site.register(Comment)
# admin.site.register(PostView)
# admin.site.register(TeamView)
admin.site.register(Team, TeamD)
