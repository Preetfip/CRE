# Generated by Django 2.1.8 on 2019-04-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listingAgent',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listingOffice',
            field=models.CharField(default='', max_length=200),
        ),
    ]