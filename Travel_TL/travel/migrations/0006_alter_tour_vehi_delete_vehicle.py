# Generated by Django 5.0.6 on 2024-05-25 07:48

import travel.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_alter_tour_vehi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='vehi',
            field=models.CharField( max_length=100),
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
