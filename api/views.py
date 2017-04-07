from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def users_new(request):
    return render(request, 'users/new.html')
