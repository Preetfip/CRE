# Generated by Django 2.1.8 on 2019-04-20 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190419_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='county',
            field=models.CharField(default='.', max_length=100),
        ),
    ]
