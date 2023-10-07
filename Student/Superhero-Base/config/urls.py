from .views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>/', HeroDetailView.as_view(), name='hero_detail'),
    path('add/', HeroCreateView.as_view(), name='hero_create'),
    path('<int:pk>/update/', HeroUpdateView.as_view(), name='hero_update'),
    path('<int:pk>/delete/', HeroDeleteView.as_view(), name='hero_delete'),
    path('admin/', admin.site.urls),
    path('heroes/', include('heroes.urls')),
    path('register/', auth_views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
