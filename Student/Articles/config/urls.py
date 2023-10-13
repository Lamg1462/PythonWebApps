from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.view_articles, name='view_articles'),

    path('articles/write/', views.write_article, name='write_article'),

    path('articles/modify/<int:article_id>/', views.modify_article, name='modify_article'),

]
