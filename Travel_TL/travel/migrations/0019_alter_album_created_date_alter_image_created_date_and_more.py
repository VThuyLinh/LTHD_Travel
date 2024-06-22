# Generated by Django 5.0.6 on 2024-06-15 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0018_alter_album_created_date_alter_image_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 15, 10, 16, 20, 36989)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 15, 10, 16, 20, 35988)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='DepartureDay',
            field=models.DateField(auto_now_add=True),
        ),
    ]
