from django.test import TestCase
from django.urls import reverse
from .models import Room, Message

class RoomTestCase(TestCase):
    def setUp(self):
        room_1 = Room.objects.create(name="Room 1", tag="Tag 1")
        room_2 = Room.objects.create(name="Room 2", tag="Tag 2")

        Message.objects.create(room = room_1, username="User 1", message="Message 1")
        Message.objects.create(room = room_1, username="User 2", message="Message 2")

    #Model Tests
    def test_rooms_exist(self):
        self.assertEqual(Room.objects.count(), 2)

    def test_messages_exist(self):
        self.assertEqual(Message.objects.count(), 2)

    def test_messages_have_rooms(self):
        room_1 = Room.objects.first()
        message_1 = Message.objects.first()

        self.assertEqual(message_1.room.name, room_1.name)
        self.assertEqual(message_1.room.tag, room_1.tag)

    def test_get_chats_returns_list(self):
        message_1 = Message.objects.first()
        message_2 = Message.objects.last()
        expected = [
            {'username': message_1.username, 'message': message_1.message, 'updated_at': message_1.updated_at},
            {'username': message_2.username, 'message': message_2.message, 'updated_at': message_2.updated_at}
        ]

        self.assertEqual(Message.get_chats(), expected)

    #routes
    def test_root_path(self):
        url = reverse('root')

        self.assertEqual(url, '/')

    def test_rooms_new_path(self):
        url = reverse('room_new')

        self.assertEqual(url, '/rooms/new')

    def test_room_detail_path(self):
        room_1 = Room.objects.first()
        url = reverse('room_detail', args=[room_1.id])

        self.assertEqual(url, '/rooms/%s' % room_1.id)

    def test_messages_path(self):
        url = reverse('message_list')

        self.assertEqual(url, '/api/v1/messages/')
