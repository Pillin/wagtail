# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0007_image_file_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(db_index=True, verbose_name='Created at', auto_now_add=True),
        ),
    ]
