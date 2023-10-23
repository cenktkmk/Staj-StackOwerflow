from django import forms
from .models import *


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
