# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_autoclassify_status'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='job',
            index_together=set([('repository', 'option_collection_hash', 'job_type', 'start_time'), ('repository', 'build_platform', 'job_type', 'start_time'), ('repository', 'submit_time'), ('machine_platform', 'option_collection_hash', 'push'), ('repository', 'build_platform', 'option_collection_hash', 'job_type', 'start_time'), ('repository', 'job_type', 'start_time')]),
        ),
    ]
