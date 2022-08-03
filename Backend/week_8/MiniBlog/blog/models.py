from datetime import datetime
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse("profile-detail", args=[self.pk])


class Bloggers(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio_info = models.TextField()

    def __str__(self) -> str:
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("blog:blogger", kwargs={"pk": self.pk})


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    post_date = models.DateTimeField()
    author = models.ForeignKey(
        Bloggers, on_delete=models.CASCADE, related_name="author", null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.title} {self.author}"

    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['post_date']


# @receiver(pre_save, sender=BlogPost)
# def slug_function(sender, instance, *args, **kwargs):
#     instance.slug = slugify(instance.title)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=400)
    post_date = models.DateField(auto_now=datetime.now())
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, null=True, related_name="comments")

    def __str__(self) -> str:
        return f"{self.post_date}"

    class Meta:
        ordering = ['post_date']
