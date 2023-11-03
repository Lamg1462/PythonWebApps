from django.test import TestCase
from .models import Superhero
from django.urls import reverse

class SuperheroTestCase(TestCase):
    def setUp(self):
        self.superhero1 = Superhero.objects.create(
            name="Hulk",
            weaknesses="Vulnerability to mind control, limited intelligence in Hulk form",
            strengths="Superhuman strength, durability, regeneration.",
            description="A brilliant scientist who, when angry, transforms into the incredible Hulk.",
            image="hulk.jpg"  
        self.superhero2 = Superhero.objects.create(
            name="Spiderman",
            weaknesses="Vulnerability to certain materials, personal life challenges.",
            strengths="Wall-crawling, web-slinging, enhanced strength, agility, danger sense.",
            description="A high school student bitten by a radioactive spider, gaining spider-like abilities.",
            image="spiderman.jpg"  
        )
        )
        
    def test_superhero_list_view(self):
        response = self.client.get(reverse('superhero_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.superhero1.name)

    def test_superhero_detail_view(self):
        response = self.client.get(reverse('superhero_detail', args=[self.superhero1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.superhero1.name)
   