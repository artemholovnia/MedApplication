# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedApp', '0014_auto_20170501_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default='2017-05-05 00:06', verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='uslugadlaclienta',
            name='cash',
            field=models.IntegerField(default=None, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='uslugadlaclienta',
            name='date',
            field=models.DateField(default='2017-05-05', verbose_name='Дата процедуры'),
        ),
        migrations.AlterField(
            model_name='uslugadlaclienta',
            name='income',
            field=models.IntegerField(default=None, verbose_name='Заработок'),
        ),
    ]
