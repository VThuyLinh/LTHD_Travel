# Generated by Django 5.0.6 on 2024-06-01 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_remove_user_avatar_alter_album_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Staff'},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='id_Customer',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='id_staff',
        ),
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 22, 32, 7, 956245)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 22, 32, 7, 956245)),
        ),
    ]
