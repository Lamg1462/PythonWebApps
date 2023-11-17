from django.test import TestCase
from django.urls import reverse
from .models import Message

class MessageModelTest(TestCase):
    def setUp(self):
        Message.objects.create(title='Test Message', text='This is a test message.')

    def test_message_str(self):
        message = Message.objects.get(title='Test Message')
        self.assertEqual(str(message), 'Test Message')

class MessageViewsTest(TestCase):
    def setUp(self):
        Message.objects.create(title='Test Message', text='This is a test message.')

    def test_message_list_view(self):
        response = self.client.get(reverse('message-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Message')

    def test_message_detail_view(self):
        message = Message.objects.get(title='Test Message')
        response = self.client.get(reverse('message-detail', args=[message.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Message')

    def test_message_create_view(self):
        response = self.client.post(reverse('message-create'), {'title': 'New Message', 'text': 'This is a new message.'})
        self.assertEqual(response.status_code, 302)  # Check if the view redirects after creating a message

    def test_message_update_view(self):
        message = Message.objects.get(title='Test Message')
        response = self.client.post(reverse('message-update', args=[message.id]), {'title': 'Updated Message', 'text': 'This is an updated message.'})
        self.assertEqual(response.status_code, 302)  # Check if the view redirects after updating a message

    def test_message_delete_view(self):
        message = Message.objects.get(title='Test Message')
        r
