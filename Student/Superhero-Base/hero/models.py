from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    strengths = models.TextField()
    weaknesses = models.TextField()
    profile_photo = models.ImageField(upload_to='superhero_photos/')
    
    def __str__(self):
        return self.name