from django.contrib import admin

from .models import BlogAuthor, BlogPost, Comment

# Register your models here


class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ("author", "post_date")
    list_display = ("title", "author", "post_date")


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("post_date",)
    list_display = ("post_date",)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogAuthor)
admin.site.register(Comment, CommentAdmin)
