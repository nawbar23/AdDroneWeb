# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20170224_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone_info',
            name='id_fly_history',
            field=models.IntegerField(),
        ),
    ]