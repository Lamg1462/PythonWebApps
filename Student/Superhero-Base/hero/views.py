from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView

from.models import Superhero

class HeroListview(ListView):
    template_name = 'hero/lists.html'
    model = Superhero


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero


class HeroCreateView(CreateView):
    template_name = "hero/create.html"
    model = Superhero
    fields = '__all__'


class HeroUpdateView(UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'


class HeroDeleteView(DeleteView):
    template_name = "hero/delete.html"
    model = Superhero
    success_url = reverse_lazy('hero_list')