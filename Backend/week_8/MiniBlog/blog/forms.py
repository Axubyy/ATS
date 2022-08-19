from dataclasses import field
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import BlogPost, Comment, Profile
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    # Metadata

    class Meta:
        fields = ['description']
        model = Comment
        labels = {'description': _('Your Comment')}


class UserUpdateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ["email", "username", "first_name", "last_name"]
        model = User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "username", "password"]


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ['image']
        # exclude = []
        model = Profile
        labels = {
            "image": " Your Profile Pix",

        }


class BlogPostCreateForm(forms.ModelForm):
    class Meta:
        fields = ["title", "description"]
        model = BlogPost
