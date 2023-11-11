from django.db import models
from django.contrib.auth.models import User

class Superhero(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Investigator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    hero = models.ForeignKey(Superhero, on_delete=models.CASCADE)
    investigator = models.ForeignKey(Investigator, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    hero = models.ForeignKey(Superhero, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo of {self.hero.name}"
