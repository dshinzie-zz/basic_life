from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Room, Message

def chats(request):
    def _get_chats():
        return [{
            'room': message.room.name,
            'handle': message.handle,
            'message': message.message
        } for message in Message.objects.all()]

    chats = _get_chats()
    return JsonResponse(chats, safe=False)
