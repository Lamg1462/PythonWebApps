from pathlib import Path
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
import json

from .models import Hero


class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }


class HeroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'hero': Hero.objects.get(pk=kwargs['pk'])
        }