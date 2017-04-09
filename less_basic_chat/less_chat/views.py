from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import JsonResponse
from .models import Room, Message
from .forms import RoomForm, MessageForm

def home(request):
    return render(request, 'home.html')

def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.updated_at = timezone.now()
            room.save()
            return redirect('root')
    else:
        form = RoomForm()
    return render(request, 'rooms/new.html', {'form': form})
