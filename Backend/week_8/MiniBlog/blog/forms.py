from dataclasses import field
from .models import Comment
from django.utils.translation import gettext_lazy as _

from django import forms


class CommentForm(forms.ModelForm):
    # Metadata

    class Meta:
        fields = ['description']
        model = Comment
        labels = {'description': _('Your Comment')}
        help_texts = {'description': _(
            'Enter what you feel about this blog post')}
