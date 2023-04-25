from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #imports default user creation form
from django import forms #imports django forms
from django.contrib.auth.models import User #uses the default django User model

#Used to register turtle
class CreateUserForm(UserCreationForm): 
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    registration_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'registration_code']






#used to update User Profile

