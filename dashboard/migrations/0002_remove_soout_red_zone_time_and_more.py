# Generated by Django 4.2 on 2023-04-30 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soout',
            name='red_zone_time',
        ),
        migrations.RemoveField(
            model_name='soout',
            name='yellow_zone_time',
        ),
    ]