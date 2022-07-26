from django.db import models

# Create your models here


class BlogAuthor(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    bio_list = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
    description = models.TextField()
    post_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.post_date}"


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    post_date = models.DateTimeField()
    author = models.ForeignKey(
        BlogAuthor, on_delete=models.CASCADE, related_name="author")
    description = models.TextField()
    comment = models.ForeignKey(
        Comment, related_name="comment", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} {self.author}"
