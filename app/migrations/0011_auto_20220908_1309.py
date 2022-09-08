# Generated by Django 3.2.15 on 2022-09-08 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220908_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='moment',
        ),
        migrations.AddField(
            model_name='task',
            name='head',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='task',
            name='tail',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='actual',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]