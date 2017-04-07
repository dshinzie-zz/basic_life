from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='root'),
    url(r'^users/new$', views.users_new, name='new_user')
]
