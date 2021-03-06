# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-02 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_auto_20180101_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_head',
            field=models.ImageField(default='articles/images/peter-pan.jpg', upload_to='articles/images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(),
        ),
    ]
