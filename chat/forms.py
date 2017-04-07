from django import forms
from .models import User, Chat

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('name', 'message',)
