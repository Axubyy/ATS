from django.contrib import admin
from django.utils.html import format_html

from .models import BlogPost, Bloggers, Comment, Profile, User

# Register your models here


class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ("author", "post_date")
    list_display = ("title", "author", "post_date")
    # prepopulated_fields = ["slug"]


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("post_date",)
    list_display = ("post_date",)


class ProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src={} width="30px" style="border-radius:50%" >'.format(object.image.url))

    thumbnail.short_description = "Profile picture"

    list_display = ["thumbnail", "user", "image"]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Bloggers)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
