from django.test import TestCase
from django.urls import reverse
from superhero_app.models import Message

class MessageInstanceTest(TestCase):
    def setUp(self):
        self.message = Message.objects.create(title='Test Message', text='This is a test message.')

    def test_message_instance(self):
        self.assertEqual(str(self.message), 'Test Message')

    def test_message_detail_view(self):
        response = self.client.get(reverse('message-detail', args=[self.message.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Message')

    def test_message_update(self):
        updated_title = 'Updated Message'
        updated_text = 'This is an updated message.'
        self.message.title = updated_title
        self.message.text = updated_text
        self.message.save()

        updated_message = Message.objects.get(pk=self.message.pk)

        self.assertEqual(updated_message.title, updated_title)
        self.assertEqual(updated_message.text, updated_text)
