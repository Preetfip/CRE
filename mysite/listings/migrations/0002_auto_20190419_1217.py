# Generated by Django 2.1.8 on 2019-04-19 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='caprate',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='expense',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='income',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='listingAgent',
            field=models.CharField(default='na', max_length=200),
        ),
        migrations.AddField(
            model_name='listing',
            name='listingOffice',
            field=models.CharField(default='na', max_length=200),
        ),
        migrations.AddField(
            model_name='listing',
            name='yearbuild',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
