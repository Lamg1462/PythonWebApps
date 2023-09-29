from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField()
    strengths = models.CharField(max_lenth=100)
    weaknesses = models.CharField(max_length=100)
    profile_photo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name