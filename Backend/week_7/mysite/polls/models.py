import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        self.pub_date >= timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name="choice", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
