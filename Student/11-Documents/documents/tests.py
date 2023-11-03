 from django.test import TestCase
from .models import Superhero, Document
from django.urls import reverse

class SuperheroDocumentTests(TestCase):
    def setUp(self):
        self.superhero = Superhero.objects.create(name='Superman', power='Flight')

    def test_superhero_creation(self):
        """Test if a superhero is created properly"""
        self.assertEqual(self.superhero.name, 'Superman')
        self.assertEqual(self.superhero.power, 'Flight')

    def test_document_creation(self):
        """Test if a document is associated with a superhero"""
        document = Document.objects.create(superhero=self.superhero, content='Sample document content')
        self.assertEqual(document.superhero, self.superhero)
        self.assertEqual(document.content, 'Sample document content')

    def test_superhero_list_view(self):
        """Test if the list view displays superheroes"""
        response = self.client.get(reverse('superhero_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Superman')

    def test_superhero_detail_view(self):
        """Test if the detail view displays superhero details and associated documents"""
        response = self.client.get(reverse('superhero_detail', args=(self.superhero.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Superman')
        self.assertContains(response, 'Sample document content')
