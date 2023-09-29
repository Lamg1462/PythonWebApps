from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from.models import Superhero

class HeroListview(ListView):
    template_name = 'hero/lists.html'
    model = Superhero