import user
from django import forms
from django.db import models
from django.forms import ModelForm
from models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'picture', 'date_of_birth')

class PatternForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Pattern
        fields = ('title', 'description', 'slug')

class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('comment_string',)
