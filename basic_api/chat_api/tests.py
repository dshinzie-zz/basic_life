from django.test import TestCase
from .models import Room, Message

class RoomTestCase(TestCase):
    def setUp(self):
        Room.objects.create(name="test", label="test")
        Room.objects.create(name="test2", label="test2")

    def test_animals_exist(self):
        self.assertEqual(Room.objects.count(), 2)

    
