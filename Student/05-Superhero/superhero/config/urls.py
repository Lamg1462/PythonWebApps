from django.contrib import admin
from django.urls import path
from hero.views import HeroDetailView, HeroListView

urlpatterns = [
    path('admin/', admin.site.urls),
 path("", HeroListView.as_view()),
    path("hero/<str:pk>", HeroDetailView.as_view())
]

