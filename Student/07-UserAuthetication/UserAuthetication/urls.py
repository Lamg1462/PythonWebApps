from django.urls import path
from . import viewsfrom
django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('create_article/', views.create_article, name='create_article'),
    path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
    path('view_article/<int:article_id>/', views.view_article, name='view_article'),
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]
