from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from .models import Superhero, Investigator, Photo

class PhotoModelTest(TestCase):
    def setUp(self):
        self.superhero = Superhero.objects.create(name="Ironman")
        self.investigator = Investigator.objects.create(user=User.objects.create_user(username="photo_investigator"))
        self.photo_image = SimpleUploadedFile("test_photo.jpg", b"file_content", content_type="image/jpeg")

    def test_create_photo(self):
        photo = Photo.objects.create(image=self.photo_image, hero=self.superhero)
        self.assertEqual(photo.hero, self.superhero)
        self.assertEqual(str(photo), "Photo of Ironman")

    def test_photo_upload_to_media(self):
        photo = Photo.objects.create(image=self.photo_image, hero=self.superhero)
        uploaded_file_path = photo.image.path
        self.assertTrue(uploaded_file_path.startswith('media/photos/'))

    def test_photo_delete(self):
        photo = Photo.objects.create(image=self.photo_image, hero=self.superhero)
        photo_id = photo.id
        photo.delete()
        with self.assertRaises(Photo.DoesNotExist):
            Photo.objects.get(id=photo_id)
