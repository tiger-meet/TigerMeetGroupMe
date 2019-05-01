from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class GroupChats(models.Model):
    GroupName = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)

class SportsEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')

class WorkingOutEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')

class VideoGamesEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')

class TransportationEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')

class ProblemSetEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')

class MiscellaneousEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50, default='filler')
    Size = models.CharField(max_length=50, default='0')