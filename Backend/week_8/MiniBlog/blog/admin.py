from re import L
from django.contrib import admin
from django.utils.html import format_html

from .models import BlogPost, Bloggers, Comment, Profile, Tag, User

# Register your models here


class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ("author", "post_date")
    list_display = ("title", "author", "post_date", "is_deleted")
    # prepopulated_fields = ["slug"]


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("post_date", 'user',)
    list_display = ("post_date", 'user',)


class ProfileAdmin(admin.ModelAdmin):
    # def thumbnail(self, object):
    #     return format_html('<img src={} width="30px" style="border-radius:50%" >'.format(object.image.url))

    # thumbnail.short_description = "Profile picture"

    list_display = ["user", "image"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Bloggers)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tag, TagAdmin)
