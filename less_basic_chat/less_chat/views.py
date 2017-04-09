from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import JsonResponse
from .models import Room, Message
from .forms import RoomForm, MessageForm

def home(request):
    pass
