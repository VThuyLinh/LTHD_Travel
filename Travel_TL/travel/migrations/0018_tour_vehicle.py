# Generated by Django 5.0.6 on 2024-05-25 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0017_transport'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='Vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.transport'),
        ),
    ]