# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedApp', '0010_auto_20170425_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default='2017-04-25 14:52', verbose_name='Дата регистрации'),
        ),
    ]
