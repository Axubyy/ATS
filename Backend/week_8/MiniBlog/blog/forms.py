from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Comment, Profile

User = get_user_model()


class CommentForm(forms.ModelForm):
    # Metadata

    class Meta:
        fields = ['description']
        model = Comment
        labels = {'description': _('Your Comment')}
        help_texts = {'description': _(
            'Enter what you feel about this blog post')}


class UserUpdateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ["first_name", "last_name", "email"]
        model = User


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ['image']
        # exclude = []
        model = Profile
        labels = {
            "image": " Your Profile Pix",

        }
