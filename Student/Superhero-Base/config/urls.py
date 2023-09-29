from django.urls import path
from .views import SuperheroListView, SuperheroDetailView, SuperheroCreateView, SuperheroUpdateView, SuperheroDeleteView

urlpatterns = [
    path('', SuperheroListView.as_view(), name='superhero_list'),
    path('detail/<int:pk>/', SuperheroDetailView.as_view(), name='superhero_detail'),
    path('create/', SuperheroCreateView.as_view(), name='superhero_create'),
    path('update/<int:pk>/', SuperheroUpdateView.as_view(), name='superhero_update'),
    path('delete/<int:pk>/', SuperheroDeleteView.as_view(), name='superhero_delete'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('superheroes.urls')),
]