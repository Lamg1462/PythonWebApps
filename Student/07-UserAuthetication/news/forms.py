from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):

    class CustomAuthenticationForm(AuthenticationForm):
