# Generated by Django 3.2.7 on 2023-04-24 05:32

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_worldborder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldborder',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326),
        ),
    ]
