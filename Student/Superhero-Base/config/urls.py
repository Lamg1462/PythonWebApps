from django.urls import path
from .views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>/', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroCreateView.as_view(), name='hero_create'),
    path('<int:pk>/', HeroUpdateView.as_view(), name='hero_update'),
    path('<int:pk>/delete', HeroDeleteView.as_view(), name='hero_delete'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('heroes.urls')),
]