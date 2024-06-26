# Generated by Django 5.0.6 on 2024-06-01 17:21

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_thumbnail',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 0, 21, 28, 748125)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 0, 21, 28, 748125)),
        ),
    ]
