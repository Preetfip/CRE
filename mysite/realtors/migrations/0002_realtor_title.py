# Generated by Django 2.1.8 on 2019-04-19 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='title',
            field=models.CharField(default='Agent', max_length=200),
        ),
    ]
