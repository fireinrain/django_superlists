# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20161221_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='listdb',
            field=models.TextField(default=''),
        ),
    ]
