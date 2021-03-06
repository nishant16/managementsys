# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('hotel', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='hotel',
            field=models.ManyToManyField(blank=True, to='hotels.Hotel'),
        ),
    ]
