# Generated by Django 5.0.6 on 2024-06-01 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 22, 11, 2, 258348)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 22, 11, 2, 258348)),
        ),
    ]
