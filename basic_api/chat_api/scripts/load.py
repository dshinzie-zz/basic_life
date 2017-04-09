import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basic_api.settings")
import django
django.setup()

from ..models import Room, Message

def load_rooms():
    for i in range(10):
        Room.objects.create(name="room %s" % i, label="label %s" % i)

def load_messages():
    for room in Room.objects.all():
        for i in range(10):
            Message.objects.create(room=room, handle="handle %s" % i, message="message %s" % i)

load_rooms()
load_messages()
