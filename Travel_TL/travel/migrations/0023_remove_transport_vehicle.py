# Generated by Django 5.0.6 on 2024-05-25 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0022_alter_tour_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='vehicle',
        ),
    ]
