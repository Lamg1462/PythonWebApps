from django.test import TestCase
from django.contrib.auth.models import User
from .models import Superhero, Investigator, Article, Photo

class SuperheroModelTest(TestCase):
    def test_str_representation(self):
        superhero = Superhero(name="Hulk")
        self.assertEqual(str(superhero), "Hulk")

class InvestigatorModelTest(TestCase):
    def test_str_representation(self):
        user = User(username="investigator_user")
        investigator = Investigator(user=user)
        self.assertEqual(str(investigator), "investigator_user")

class ArticleModelTest(TestCase):
    def test_str_representation(self):
        superhero = Superhero(name="Spiderman")
        investigator = Investigator(user=User(username="article_investigator"))
        article = Article(title="Spiderman's Adventures", content="Some content", hero=superhero, investigator=investigator)
        self.assertEqual(str(article), "Spiderman's Adventures")

class PhotoModelTest(TestCase):
    def test_str_representation(self):
        superhero = Superhero(name="Black Widow")
        photo = Photo(image="path/to/photo.jpg", hero=superhero)
        self.assertEqual(str(photo), "Photo of Black Widow")
