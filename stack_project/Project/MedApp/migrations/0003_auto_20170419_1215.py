# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedApp', '0002_auto_20170419_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='info',
            field=models.TextField(default='none', max_length=100, verbose_name='Дополнительно'),
        ),
    ]