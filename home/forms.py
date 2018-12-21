from django.contrib.auth.models import User
from .models import UserInfo
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'city']


