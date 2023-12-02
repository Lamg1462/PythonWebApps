from django.db import models

class Superhero(models.Model):
    title = models.CharField(max_length=200)
    realName = models.CharField(max_length=200)
    strength1 = models.CharField(max_length=200)
    strength2 = models.CharField(max_length=200)
    strength3 = models.CharField(max_length=200)
    weakness1 = models.CharField(max_length=200)
    weakness2 = models.CharField(max_length=200)
    weakness3 = models.CharField(max_length=200)
    imagePath = models.CharField(max_length=200)
    def _str_(self):
        return f'{self.pk}. {self.name} - {self.description}'