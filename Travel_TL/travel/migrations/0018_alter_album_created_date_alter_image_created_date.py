# Generated by Django 5.0.6 on 2024-06-15 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0017_remove_schedule_departuretime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 15, 10, 13, 57, 547230)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
