# Generated by Django 5.1 on 2024-09-13 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autowash', '0020_alter_sensordata_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemstatus',
            name='user',
        ),
    ]
