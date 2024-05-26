# Generated by Django 5.0.6 on 2024-05-26 04:05

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0035_tour_description_alter_image_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cmt_news',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='cmt_tour',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 26, 11, 5, 42, 906074)),
        ),
    ]
