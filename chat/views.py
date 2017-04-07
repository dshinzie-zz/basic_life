from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import JsonResponse
from .forms import UserForm
from .models import User

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users })

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
