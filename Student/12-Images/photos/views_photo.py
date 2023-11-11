from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Photo
from .forms import PhotoForm

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
