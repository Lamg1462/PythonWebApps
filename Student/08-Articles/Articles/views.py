from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article

@login_required
def write_article(request):
    if request.method == 'POST':
        return render(request, 'write_article.html')

def view_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

@login_required
def modify_article(request, article_id):
    