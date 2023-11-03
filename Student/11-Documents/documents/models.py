from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    power = models.CharField(max_length=100)

class Document(models.Model):
    superhero = models.ForeignKey(Superhero, on_delete=models.CASCADE)
    content = models.TextField()
