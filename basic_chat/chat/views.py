from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import JsonResponse
from .forms import UserForm, ChatForm
from .models import User, Chat
from django.core import serializers

def home(request):
    users = User.objects.all()
    chats = Chat.objects.all()
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.published_date = timezone.now()
            chat.save()
    else:
        form = ChatForm()
    return render(request, 'home.html', {'users': users, 'form': form, 'chats': chats })

def users_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.published_date = timezone.now()
            user.save()
            return redirect('root')
    else:
        form = UserForm()
    return render(request, 'users/new.html', {'form': form})

def chats(request):
    def _get_chats():
        return [{
            'name': chat.name,
            'message': chat.message,
            'published_date': chat.published_date
        } for chat in Chat.objects.order_by("published_date")]
    chats = _get_chats()
    return JsonResponse(chats, safe=False)

def chats_new(request):
    form = ChatForm(request.POST)
    if form.is_valid():
        if form.is_valid():
            user = form.save(commit=False)
            user.published_date = timezone.now()
            user.save()
    return render(request, 'users/new.html', {'form': form})
