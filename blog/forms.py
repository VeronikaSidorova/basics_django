from django import forms
from django.forms import ModelForm

from catalog.forms import StyleFormMixin
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = (
            "title",
            "content",
            "preview_image",
            "is_published",
        )


class PostModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = BlogPost
        exclude = ("created_at",)
