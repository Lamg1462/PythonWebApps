from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=200, default ="None")
    identity = models.TextField(default ="None")
    description = models.TextField(default="None")
    strengths = models.TextField(default="None")
    weaknesses = models.TextField(default="None")
    image = models.ImageField(upload_to='superhero_images/', default ="None")
    
    def __str__(self):
        return self.name