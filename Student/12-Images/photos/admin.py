from django.contrib import admin
from .models import Superhero, Investigator, Article, Photo

class SuperheroAdmin(admin.ModelAdmin):
    list_display = ('name',)

class InvestigatorAdmin(admin.ModelAdmin):
    list_display = ('user',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'hero', 'investigator',)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'hero',)

admin.site.register(Superhero, SuperheroAdmin)
admin.site.register(Investigator, InvestigatorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Photo, PhotoAdmin)
