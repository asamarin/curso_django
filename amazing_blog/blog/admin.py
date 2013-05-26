from django.contrib import admin
from models import Post, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'intro', 'mas')
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
