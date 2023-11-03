from django.test import TestCase
from .models import Hero, Article
import csv
from io import StringIO

class HeroTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name="Hulk", real_name="Bruce Banner", powers="Superhuman strength")
        Hero.objects.create(name="Spiderman", real_name="Peter Parker", powers="Wall-crawling, Web-slinging")

    def test_adding_records(self):
        hulk = Hero.objects.get(name="Hulk")
        spiderman = Hero.objects.get(name="Spiderman")
        self.assertEqual(hulk.name, "Hulk")
        self.assertEqual(spiderman.name, "Spiderman")

    def test_query_all_records(self):
        all_heroes = Hero.objects.all()
        self.assertEqual(all_heroes.count(), 2)

    def test_serialization_to_csv(self):
        heroes = Hero.objects.all()
        csv_buffer = StringIO()
        writer = csv.writer(csv_buffer)
        for hero in heroes:
            writer.writerow([hero.id, hero.name, hero.real_name, hero.powers])
        csv_content = csv_buffer.getvalue()

    def test_saving_reading_file(self):
        with open("test_heroes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            heroes = Hero.objects.all()
            for hero in heroes:
                writer.writerow([hero.id, hero.name, hero.real_name, hero.powers])

        with open("test_heroes.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:

    def test_deserialization_from_csv(self):
        with open("test_heroes.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:

    def test_creation_existing_objects(self):
        hero = Hero.objects.create(name="Ironman", real_name="Tony Stark", powers="Powered armor suit")
        self.assertEqual(hero.name, "Ironman")

    def test_complete_round_trip(self):
        heroes = Hero.objects.all()
        csv_buffer = StringIO()
        writer = csv.writer(csv_buffer)
        for hero in heroes:
            writer.writerow([hero.id, hero.name, hero.real_name, hero.powers])
        csv_content = csv_buffer.getvalue()

        with open("test_heroes.csv", "w", newline="") as file:
            file.write(csv_content)

        with open("test_heroes.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
