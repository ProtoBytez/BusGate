# Generated by Django 3.2.7 on 2021-10-05 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gate', '0005_locations_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='ph',
            field=models.IntegerField(null=True),
        ),
    ]
