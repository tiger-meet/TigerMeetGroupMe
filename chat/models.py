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
    UserId = models.CharField(max_length=50, null=True)

class WorkingOutEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    UserId = models.CharField(max_length=50, null=True)

class VideoGamesEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    UserId = models.CharField(max_length=50, null=True)

class TransportationEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    UserId = models.CharField(max_length=50, null=True)

class ProblemSetEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    UserId = models.CharField(max_length=50, null=True)

class MiscellaneousEvents(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    UserId = models.CharField(max_length=50, null=True)