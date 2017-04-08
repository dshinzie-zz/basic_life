from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^api/v1/chats$', views.chats, name='chats')
]
