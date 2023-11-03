from django.contrib import admin
from .models import Superhero, Article

@admin.register(Superhero)
class SuperheroAdmin(admin.ModelAdmin):
    list_display = ('name',) 

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')  
    list_filter = ('author',)  
    search_fields = ('title', 'author__username')  
    prepopulated_fields = {'slug': ('title',)}  

    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='published')

    make_published.short_description = 'Mark selected articles as published'  
