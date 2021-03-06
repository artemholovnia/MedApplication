# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 12:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MedApp', '0007_auto_20170419_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usluga',
            name='info',
        ),
        migrations.RemoveField(
            model_name='uslugadlaclienta',
            name='method_cash',
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usluga',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='uslugadlaclienta',
            name='income',
            field=models.IntegerField(default=0, verbose_name='Заработок'),
        ),
        migrations.AddField(
            model_name='uslugadlaclienta',
            name='medicine',
            field=models.CharField(default='none', max_length=30, verbose_name='Название препарата'),
        ),
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2017, 4, 20, 14, 28, 14, 17400), verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='uslugadlaclienta',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 4, 20, 14, 28, 14, 20400), verbose_name='Дата процедуры'),
        ),
    ]
