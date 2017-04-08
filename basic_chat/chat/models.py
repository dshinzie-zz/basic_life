from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

class Chat(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
