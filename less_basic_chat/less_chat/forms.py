from django import forms
from .models import Room, Message

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'tag')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('username', 'message')
