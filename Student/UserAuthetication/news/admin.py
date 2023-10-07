from django.contrib import admin

from django.contrib import admin
from .models import Superhero

@admin.register(Superhero)
class SuperheroAdmin(admin.ModelAdmin):
    list_display = ('name', 'identity', 'strength', 'weakness', 'author')
    list_filter = ('strength', 'weakness')
    search_fields = ('name', 'identity')
    list_per_page = 20  

    ordering = ('name',)

