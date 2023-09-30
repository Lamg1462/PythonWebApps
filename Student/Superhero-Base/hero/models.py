from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=200, default ="None")
    identity = models.CharField(max_length=200, default ="None")
    description = models.TextField(default="None")
    strengths = models.CharField(max_length=200, default ="None")
    weaknesses = models.CharField(max_length=200, default ="None")
    image = models.CharField(max_length=200, default ="None")
    
    def __str__(self):
        return self.name