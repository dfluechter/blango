from django.contrib import admin
from .models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'published_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('creator', 'content', 'created_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('value',)
