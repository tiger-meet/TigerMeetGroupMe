# Generated by Django 2.1.7 on 2019-05-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20190423_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscellaneousevents',
            name='ShareToken',
        ),
        migrations.AddField(
            model_name='miscellaneousevents',
            name='Size',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='problemsetevents',
            name='Size',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='sportsevents',
            name='Size',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='transportationevents',
            name='Size',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='videogamesevents',
            name='Size',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='workingoutevents',
            name='Size',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
