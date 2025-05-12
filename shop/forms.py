from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your first name'})
    )
    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your last name'})
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your email'})
    )
    username = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your username'})
    )
    password1 = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={'name' : 'password', 'type' : 'password', 'class' : 'form-control', 'placeholder' : 'Enter your password'})
    )
    password2 = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={'name' : 'password', 'type' : 'password', 'class' : 'form-control', 'placeholder' : 'Enter your password again'})
    )

    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2' )