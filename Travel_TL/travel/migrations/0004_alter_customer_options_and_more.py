# Generated by Django 5.0.6 on 2024-06-01 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_alter_staff_options_remove_customer_id_customer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer'},
        ),
        migrations.AlterUniqueTogether(
            name='cmt_news',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='cmt_tour',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 22, 48, 28, 726050)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 22, 48, 28, 726050)),
        ),
        migrations.AlterUniqueTogether(
            name='rating_tour',
            unique_together={('tour', 'user')},
        ),
    ]
