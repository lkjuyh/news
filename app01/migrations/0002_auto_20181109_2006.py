# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-09 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default='lu.gif', max_length=255, upload_to='image/%Y/%m', verbose_name='头像'),
        ),
    ]
