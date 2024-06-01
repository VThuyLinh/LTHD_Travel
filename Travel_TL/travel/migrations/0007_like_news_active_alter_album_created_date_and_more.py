# Generated by Django 5.0.6 on 2024-06-01 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_news_active_alter_album_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='like_news',
            name='Active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 1, 24, 26, 540413)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 1, 24, 26, 541456)),
        ),
    ]