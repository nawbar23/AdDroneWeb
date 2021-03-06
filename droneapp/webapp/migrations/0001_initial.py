# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-24 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drone_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controller_state', models.CharField(max_length=30)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('velocity', models.FloatField()),
                ('batery', models.FloatField()),
                ('timestamp', models.DateField()),
                ('id_fly_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Drone_info')),
            ],
        ),
        migrations.CreateModel(
            name='Fly_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateField()),
                ('time_end', models.DateField(null=True)),
            ],
        ),
    ]
