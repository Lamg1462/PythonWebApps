
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Investigator

class UserRegisterView(CreateView):
    template_name = 'superheroes/user_register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'superheroes/user_login.html'

class UserLogoutView(LogoutView):
    template_name = 'superheroes/user_logout.html'
