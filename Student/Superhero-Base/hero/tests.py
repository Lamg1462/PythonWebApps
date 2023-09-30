from django.test import TestCase
from .models import Superhero
from django.urls import reverse

class SuperheroTestCase(TestCase):
    def setUp(self):
        self.superhero1 = Superhero.objects.create(
            name="Superhero 1",
            weaknesses="Weakness 1",
            strengths="Strength 1",
            description="Description 1",
            image="superhero1.jpg"  
        )
        
    def test_superhero_list_view(self):
        response = self.client.get(reverse('superhero_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.superhero1.name)

    def test_superhero_detail_view(self):
        response = self.client.get(reverse('superhero_detail', args=[self.superhero1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.superhero1.name)
   