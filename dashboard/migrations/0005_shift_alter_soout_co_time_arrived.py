# Generated by Django 4.2 on 2023-05-02 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_soout_co_time_arrived'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yellow_start', models.TimeField(blank=True, default=datetime.time(6, 15), null=True, verbose_name='Yellow Start')),
                ('red_start', models.TimeField(blank=True, default=datetime.time(5, 0), null=True, verbose_name='Red Start')),
            ],
        ),
        migrations.AlterField(
            model_name='soout',
            name='co_time_arrived',
            field=models.TimeField(blank=True, default=datetime.time(8, 4, 20, 590698), null=True, verbose_name='Time Arrived'),
        ),
    ]
