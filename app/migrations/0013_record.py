# Generated by Django 3.2.15 on 2022-09-08 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_task_tail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moment', models.DateTimeField(default=datetime.datetime.now)),
                ('ip', models.TextField()),
                ('token', models.TextField()),
            ],
        ),
    ]
