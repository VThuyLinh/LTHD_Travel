# Generated by Django 5.0.6 on 2024-05-26 03:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0032_album_image_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 26, 10, 2, 58, 404570)),
        ),
    ]
