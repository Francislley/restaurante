# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-21 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import restaurant.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20160820_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='added_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=100)),
                ('quantity', restaurant.models.IntegerRangeField()),
            ],
        ),
        migrations.AlterField(
            model_name='orderspecial',
            name='photo',
            field=models.ImageField(upload_to=b'order_pics/'),
        ),
    ]
