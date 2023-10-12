from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["username", "email", "password"]
