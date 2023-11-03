from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Superhero
from django.urls import reverse_lazy

class SuperheroListView(ListView):
    model = Superhero
    template_name = 'superheroes/superhero_list.html'
    context_object_name = 'superheroes'

class SuperheroDetailView(DetailView):
    model = Superhero
    template_name = 'superheroes/superhero_detail.html'
    context_object_name = 'superhero'

class SuperheroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'superheroes/superhero_form.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SuperheroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'superheroes/superhero_form.html'
    fields = '__all__'

class SuperheroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'superheroes/superhero_confirm_delete.html'
    success_url = reverse_lazy('superhero_list')
