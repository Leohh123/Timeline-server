# Generated by Django 3.2.15 on 2022-09-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220918_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stage',
            name='type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]