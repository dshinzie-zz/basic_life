from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name="room")
    username = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    @classmethod
    def get_chats(cls):
        return [{
            'username': message.username,
            'message': message.message,
            'updated_at': message.updated_at
        } for message in Message.objects.order_by("created_at")]
