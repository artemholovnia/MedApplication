# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.IntegerField(default='+380', verbose_name='Номер телефона'),
        ),
    ]
