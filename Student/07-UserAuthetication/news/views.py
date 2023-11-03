# news/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Article

def register(request):

def user_login(request):
   

@login_required
def create_article(request):

@login_required
def edit_article(request, article_id):

def view_article(request, article_id):



