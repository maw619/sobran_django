# Generated by Django 4.2 on 2023-05-02 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_soout_red_zone_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soout',
            name='co_time_arrived',
            field=models.TimeField(blank=True, default=datetime.time(1, 53, 17, 879437), null=True, verbose_name='Time Arrived'),
        ),
    ]
