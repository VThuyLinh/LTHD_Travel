# Generated by Django 5.0.6 on 2024-05-25 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0027_alter_tour_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='vehicle',
            field=models.ForeignKey(default='____', null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.transport'),
        ),
    ]
