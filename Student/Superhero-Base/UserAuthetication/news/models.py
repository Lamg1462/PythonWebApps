from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class Author(AbstractUser):
    pass

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
