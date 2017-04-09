from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="root"),
    url(r'^rooms/new$', views.room_new, name="room_new"),
]
