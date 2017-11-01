# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedApp', '0012_auto_20170425_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uslugadlaclienta',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(default='2000-12-31', verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.IntegerField(default='NULL', verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default='2017-05-01 23:36', verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='uslugadlaclienta',
            name='date',
            field=models.DateField(default='2017-05-01', verbose_name='Дата процедуры'),
        ),
    ]