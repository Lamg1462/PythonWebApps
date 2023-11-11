from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Superhero, Investigator, Article, Photo
from .forms import PhotoForm  

class SuperheroListView(ListView):
    model = Superhero
    template_name = 'superheroes/superhero_list.html'

class SuperheroDetailView(DetailView):
    model = Superhero
    template_name = 'superheroes/superhero_detail.html'

class SuperheroCreateView(CreateView):
    model = Superhero
    template_name = 'superheroes/superhero_form.html'
    fields = ['name'] 

class SuperheroUpdateView(UpdateView):
    model = Superhero
    template_name = 'superheroes/superhero_form.html'
    fields = ['name'] 

class SuperheroDeleteView(DeleteView):
    model = Superhero
    template_name = 'superheroes/superhero_confirm_delete.html'
    success_url = reverse_lazy('superhero-list')

class InvestigatorListView(ListView):
    model = Investigator
    template_name = 'superheroes/investigator_list.html'

class InvestigatorDetailView(DetailView):
    model = Investigator
    template_name = 'superheroes/investigator_detail.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'superheroes/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'superheroes/article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'superheroes/article_form.html'
    fields = ['title', 'content', 'hero', 'investigator']  

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'superheroes/article_form.html'
    fields = ['title', 'content', 'hero', 'investigator'] 

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'superheroes/article_confirm_delete.html'
    success_url = reverse_lazy('article-list')

class PhotoListView(ListView):
    model = Photo
    template_name = 'superheroes/photo_list.html'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'superheroes/photo_detail.html'

class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'superheroes/photo_form.html'
    form_class = PhotoForm

class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'superheroes/photo_form.html'
    form_class = PhotoForm

class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'superheroes/photo_confirm_delete.html'
    success_url = reverse_lazy('photo-list')
