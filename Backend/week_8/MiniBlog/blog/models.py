from datetime import datetime
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile-detail", args=[self.pk])


class Bloggers(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio_info = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.username}"

    def get_absolute_url(self):
        return reverse("blog:blogger", kwargs={"pk": self.pk})


class AvailableBlogs(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Bloggers, on_delete=models.CASCADE, related_name="author", null=True)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    objects = models.Manager()
    available_posts = AvailableBlogs()

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return f"{self.title} {self.author}"

    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['post_date']


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(pre_save, sender=BlogPost)
# def slug_function(sender, instance, *args, **kwargs):
#     instance.slug = slugify(instance.title)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=400)
    post_date = models.DateField(auto_now=datetime.now())
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, null=True, related_name="comments")
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user}"

    def get_username(self):
        return self.user

    def get_absolute_url(self):
        return reverse("blog:delete-comment", args=[self.post.pk, self.pk])

    class Meta:
        ordering = ['post_date']
