from django.urls import path
from .views import (
    SuperheroListView,
    SuperheroDetailView,
    SuperheroCreateView,
    SuperheroUpdateView,
    SuperheroDeleteView,
    InvestigatorListView,
    InvestigatorDetailView,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    PhotoListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
)

urlpatterns = [
    path('superheroes/', SuperheroListView.as_view(), name='superhero-list'),
    path('superheroes/<int:pk>/', SuperheroDetailView.as_view(), name='superhero-detail'),
    path('superheroes/new/', SuperheroCreateView.as_view(), name='superhero-create'),
    path('superheroes/<int:pk>/edit/', SuperheroUpdateView.as_view(), name='superhero-update'),
    path('superheroes/<int:pk>/delete/', SuperheroDeleteView.as_view(), name='superhero-delete'),

    path('investigators/', InvestigatorListView.as_view(), name='investigator-list'),
    path('investigators/<int:pk>/', InvestigatorDetailView.as_view(), name='investigator-detail'),

    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/new/', ArticleCreateView.as_view(), name='article-create'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-update'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),

    path('photos/', PhotoListView.as_view(), name='photo-list'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('photos/new/', PhotoCreateView.as_view(), name='photo-create'),
    path('photos/<int:pk>/edit/', PhotoUpdateView.as_view(), name='photo-update'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
]
