from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import BlogPost, Comment, Profile

User = get_user_model()


class CommentForm(forms.ModelForm):
    # Metadata

    class Meta:
        fields = ['description']
        model = Comment
        labels = {'description': _('Your Comment')}


class UserUpdateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ["email", "username"]
        model = User


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
