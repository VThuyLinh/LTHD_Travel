# Generated by Django 5.0.6 on 2024-06-01 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_news_image_thumbnail_alter_album_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 0, 36, 28, 198433)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 0, 36, 28, 199433)),
        ),
    ]