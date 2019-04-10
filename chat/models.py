from django.db import models

class GroupChats(models.Model):
    GroupName = models.CharField(max_length=50)
    GroupId = models.CharField(max_length=50)
    ShareToken = models.CharField(max_length=50)
