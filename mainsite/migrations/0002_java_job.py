# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-26 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='java_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionId', models.CharField(max_length=30)),
                ('companyFullName', models.CharField(max_length=100)),
                ('detail_url', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('workYear', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('createTime', models.CharField(max_length=30)),
                ('positionLables', models.CharField(max_length=200)),
                ('positionDetail', models.TextField()),
                ('firstType', models.CharField(max_length=200)),
                ('secondType', models.CharField(max_length=200)),
            ],
        ),
    ]