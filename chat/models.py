from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class GroupChats(models.Model):
    GroupName = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)

class Todo(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    eventTime = models.DateTimeField(default=datetime.now, blank=True)