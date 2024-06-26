# Generated by Django 5.0.6 on 2024-06-12 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0015_alter_album_created_date_alter_image_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 12, 16, 0, 41, 61925)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 12, 16, 0, 41, 60880)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='DepartureDay',
            field=models.DateField(auto_now_add=True),
        ),
    ]
