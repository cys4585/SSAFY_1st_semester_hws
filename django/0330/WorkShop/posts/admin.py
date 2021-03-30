from django.contrib import admin
from .models import Pick, Comment, Post

# Register your models here.
class PickAdmin(admin.ModelAdmin):
    list_display = ('post', 'content',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue_a', 'issue_b',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'pick', 'content')

admin.site.register(Pick, PickAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)