from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Superhero, Article

class SuperheroModelTestCase(TestCase):
    def test_superhero_model(self):
        superhero = Superhero(name="Superman")
        self.assertEqual(str(superhero), "Superman")

class ArticleModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('testuser', password='testpassword')
        self.article = Article(title="Test Article", content="This is a test.", author=user)

    def test_article_model(self):
        self.assertEqual(str(self.article), "Test Article")

class ViewsTestCase(TestCase):
    def test_view_articles(self):
        response = self.client.get(reverse('view_articles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles.html')

    def test_write_article(self):
        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.get(reverse('write_article'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'write_article.html')


    def test_modify_article(self):
        user = User.objects.create_user('testuser', password='testpassword')
        article = Article.objects.create(title="Test Article", content="This is a test.", author=user)

        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('modify_article', args=[article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modify_article.html')
