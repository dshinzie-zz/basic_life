from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='root'),
    url(r'^users/new$', views.users_new, name='new_user'),
    url(r'^api/v1/chats$', views.chats, name='chats'),
    url(r'^api/v1/chats/new$', views.chats_new, name='chats_new'),
]
