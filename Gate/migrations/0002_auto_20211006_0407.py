# Generated by Django 3.2.7 on 2021-10-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False,
    dependencies = [
        ('Gate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='busgateinfo',
            name='citys',
            field=models.ManyToManyField(to='Gate.Citys'),
        ),
    ]
