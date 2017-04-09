from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="root"),
    url(r'^rooms/new$', views.room_new, name="room_new"),
    url(r'^rooms/(?P<pk>\d+)$', views.room_detail, name="room_detail"),
    url(r'^messages/$', views.message_list, name="message_list"),
]
