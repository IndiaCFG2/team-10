from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Role_CHOICES

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # //role = forms.CharField(max_length=6, choices=Role_CHOICES, default='PM')
    class Meta:
        model = User
        fields=['username','email','password1','password2']

