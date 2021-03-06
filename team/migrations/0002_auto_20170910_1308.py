# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin',
            field=models.URLField(max_length=250),
        ),
        migrations.AlterField(
            model_name='team',
            name='pic',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='media/team/', width_field='width_field'),
        ),
    ]
