# Generated by Django 5.0.6 on 2024-05-25 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_transport_remove_tour_vehicle_tour_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='Vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.transport'),
        ),
    ]
