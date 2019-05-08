from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class GroupChats(models.Model):
    GroupName = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)

class SportsEvents(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50, default='')
    date = models.DateField()
    time = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=5000, default='')
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')
    MakerToken = models.CharField(max_length=50, default='filler')
    CategoryName = models.CharField(max_length=50, default='sports')

class WorkingOutEvents(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50, default='')
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=5000, default='')
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')
    MakerToken = models.CharField(max_length=50, default='filler')
    CategoryName = models.CharField(max_length=50, default='workingout')


class VideoGamesEvents(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50, default='')
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=5000, default='')
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')
    MakerToken = models.CharField(max_length=50, default='filler')
    CategoryName = models.CharField(max_length=50, default='videogames')

class TransportationEvents(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50, default='')
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=5000, default='')
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')
    MakerToken = models.CharField(max_length=50, default='filler')
    CategoryName = models.CharField(max_length=50, default='transportation')

class ProblemSetEvents(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50, default='')
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=5000, default='')
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='0')
    MakerToken = models.CharField(max_length=50, default='filler')
    CategoryName = models.CharField(max_length=50, default='problemset')

class MiscellaneousEvents(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50, default='')
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=5000, default='')
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50, default='filler')
    Size = models.CharField(max_length=50, default='0')
    MakerToken = models.CharField(max_length=50, default='filler')
    CategoryName = models.CharField(max_length=50, default='miscellaneous')
