from django.shortcuts import render
from .models import Superhero, Document

def superhero_list(request):
    superheroes = Superhero.objects.all()
    return render(request, 'superheroes.html', {'superheroes': superheroes})

def superhero_detail(request, superhero_id):
    superhero = Superhero.objects.get(pk=superhero_id)
    documents = Document.objects.filter(superhero=superhero)
    return render(request, 'superhero_detail.html', {'superhero': superhero, 'documents': documents})
