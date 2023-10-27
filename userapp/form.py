from django import forms
from .models import *




class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "tagleri"]


class YourModelForm(forms.ModelForm):


    class Meta:
        model = Answer
        fields = ['description', 'kodalanı']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["description"]        

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Comments2
        fields = ["description"]            
