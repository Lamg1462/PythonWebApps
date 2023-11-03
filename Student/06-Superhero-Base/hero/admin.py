from django.contrib import admin
from django.contrib import admin
from .models import Superhero

@admin.register(Superhero)
class SuperheroAdmin(admin.ModelAdmin):
    list_display = ('name', 'strengths', 'weaknesses', 'description') 
    search_fields = ('name',)